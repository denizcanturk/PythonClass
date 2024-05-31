import numpy as np
from PIL import Image
from stl.mesh import Mesh
import pymeshlab

def convert_image_to_stl(image_path, output_path, target_size=(100, 100), max_file_size=10*1024*1024):
    try:
        # Load the image
        image = Image.open(image_path)
        
        # Resize image to target size
        image = image.resize(target_size, Image.LANCZOS)
        
        # Convert image to grayscale
        gray_image = image.convert('L')
        
        # Convert grayscale image to numpy array
        height_map = np.array(gray_image)
        
        # Get image dimensions
        rows, cols = height_map.shape
        
        # Create vertices
        vertices = []
        for r in range(rows):
            for c in range(cols):
                vertices.append([c, r, height_map[r, c]])
        
        # Create faces
        faces = []
        for r in range(rows - 1):
            for c in range(cols - 1):
                # Define the corners of the quad
                v1 = r * cols + c
                v2 = r * cols + (c + 1)
                v3 = (r + 1) * cols + (c + 1)
                v4 = (r + 1) * cols + c
                
                # Create two triangles for the quad
                faces.append([v1, v2, v3])
                faces.append([v1, v3, v4])
        
        # Convert vertices and faces to numpy arrays
        vertices = np.array(vertices)
        faces = np.array(faces)
        
        # Create the mesh
        stl_mesh = Mesh(np.zeros(faces.shape[0], dtype=Mesh.dtype))
        for i, f in enumerate(faces):
            for j in range(3):
                stl_mesh.vectors[i][j] = vertices[f[j], :]
        
        # Save the initial mesh to an STL file
        stl_mesh.save('initial_output.stl')

        # Load the STL file with pymeshlab and simplify it
        ms = pymeshlab.MeshSet()
        ms.load_new_mesh('initial_output.stl')
        
        # Simplify the mesh using quadratic edge collapse decimation
        ms.apply_filter('meshing_decimation_quadric_edge_collapse', targetfacenum=int(len(faces) * 0.1))
        
        # Save the simplified mesh
        ms.save_current_mesh(output_path)
        
        # Check file size and adjust if necessary
        while os.path.getsize(output_path) > max_file_size:
            ms.apply_filter('meshing_decimation_quadric_edge_collapse', targetfacenum=int(ms.current_mesh().face_number() * 0.9))
            ms.save_current_mesh(output_path)
        
        print(f"STL file saved to {output_path}, size: {os.path.getsize(output_path) / (1024 * 1024):.2f} MB")

    except ImportError as e:
        print(f"Error importing module: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
import os

image_path = '/home/debinci/Desktop/proje/Oynamalik/FunFacts.png'
output_path = 'output.stl'
convert_image_to_stl(image_path, output_path, target_size=(100, 100))
