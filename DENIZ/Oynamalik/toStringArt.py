#pip install numpy pillow opencv-python numpy-stl pymeshlab
import numpy as np
from PIL import Image
import cv2
from stl import mesh
import pymeshlab
import os

def image_to_string_art(image_path, output_path, num_pins=200, radius=100, image_size=(500, 500)):
    # Load and preprocess the image
    image = Image.open(image_path).convert('L')
    image = image.resize(image_size)
    image = np.array(image)
    
    # Edge detection using Canny
    edges = cv2.Canny(image, 100, 200)
    
    # Create pins around a circular frame
    theta = np.linspace(0, 2 * np.pi, num_pins, endpoint=False)
    pins = np.array([(int(radius * np.cos(t) + image_size[0] / 2), int(radius * np.sin(t) + image_size[1] / 2)) for t in theta])

    # Find the closest edge points to the pins
    string_path = []
    for i in range(num_pins):
        for j in range(i + 1, num_pins):
            line = create_line(pins[i], pins[j], image_size)
            if np.any(edges[line[:, 1].astype(int), line[:, 0].astype(int)]):
                string_path.append((i, j))
    
    # Generate the 3D mesh from the string path
    vertices = []
    faces = []
    for i, (start, end) in enumerate(string_path):
        p1, p2 = pins[start], pins[end]
        vertices.append([*p1, 0])
        vertices.append([*p2, 0])
        if i > 0:
            faces.append([i*2-2, i*2-1, i*2])
            faces.append([i*2-1, i*2, i*2+1])
    
    vertices = np.array(vertices)
    faces = np.array(faces)

    # Create the mesh
    stl_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            stl_mesh.vectors[i][j] = vertices[f[j], :]
    
    # Save the initial mesh to an STL file
    stl_mesh.save('initial_output.stl')

    # Load the STL file with pymeshlab to repair and simplify it
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh('initial_output.stl')
    
    # Print the list of available filters
    print(ms.print_filter_list())
    
    # Repair non-manifold edges and faces
    ms.apply_filter('remove_non_manifold_edges')
    ms.apply_filter('remove_duplicate_vertices')
    
    # Simplify the mesh if necessary
    target_face_num = max(3, int(len(faces) * 0.5))  # Ensure a minimum of 3 faces
    ms.apply_filter('simplify', targetfacenum=target_face_num)

    # Save the repaired and simplified mesh
    ms.save_current_mesh(output_path)

    # Ensure the file size is within limits
    max_size = 10 * 1024 * 1024  # 10 MB
    while os.path.getsize(output_path) > max_size:
        # Simplify the mesh further if necessary
        target_face_num = max(3, int(ms.current_mesh().face_number() * 0.9))
        ms.apply_filter('simplify', targetfacenum=target_face_num)
        ms.save_current_mesh(output_path)
    
    print(f"STL file saved to {output_path}, size: {os.path.getsize(output_path) / (1024 * 1024):.2f} MB")

def create_line(p1, p2, image_size):
    # Bresenham's line algorithm
    p1 = np.array(p1)
    p2 = np.array(p2)
    line = []
    steep = abs(p2[1] - p1[1]) > abs(p2[0] - p1[0])
    if steep:
        p1 = p1[::-1]
        p2 = p2[::-1]
    if p1[0] > p2[0]:
        p1, p2 = p2, p1
    dx = p2[0] - p1[0]
    dy = abs(p2[1] - p1[1])
    error = dx / 2.0
    ystep = 1 if p1[1] < p2[1] else -1
    y = int(p1[1])
    for x in range(int(p1[0]), int(p2[0]) + 1):
        coord = (y, x) if steep else (x, y)
        if 0 <= coord[0] < image_size[1] and 0 <= coord[1] < image_size[0]:
            line.append(coord)
        error -= dy
        if error < 0:
            y += ystep
            error += dx
    return np.array(line)

# Usage example
image_path = '/home/debinci/Desktop/proje/Oynamalik/cat.jpeg'
output_path = 'output_string_art.stl'
image_to_string_art(image_path, output_path)
