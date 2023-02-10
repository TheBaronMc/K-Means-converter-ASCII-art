import random
import string
import argparse

from PIL import Image


def kmeans(points, k):
    # Choose random centroids
    nb_points = len(points)
    centroids = [ points[random.randint(0, nb_points-1)] for _ in range(k) ]
    
    while True:
        # Dispatch points into groups
        groups = [ [] for _ in range(k) ]
        for point in points:
            distances = [] 
            for centroid in centroids:
                distances.append(((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2 + + (centroid[2]-point[2])**2)**(1/2))
            groups[distances.index(min(distances))].append(point)
                                 
        # Compute new centroids
        new_centroids = []
        for i in range(k):
            Xsum = 0
            Ysum = 0
            Zsum = 0
            for point in groups[i]:
                Xsum += point[0]
                Ysum += point[1]
                Zsum += point[2]
            nb_points = len(groups[i])
            if nb_points > 0:
                new_centroids.append([Xsum/nb_points, Ysum/nb_points, Zsum/nb_points])
        
        # Condition to exit
        if centroids == new_centroids:
            return centroids
        else:
            centroids = new_centroids 


# Thanks to https://tech-algorithm.com/articles/nearest-neighbor-image-scaling/
def nearest_neighbor(points, w1, h1, w2, h2):
    temp = []

    x_ratio = w1//w2 
    y_ratio = h1//h2

    x2, y2 = 0, 0
    for i in range(0, int(h2)):
        for j in range(0,int(w2)):
            x2 = j*x_ratio
            y2 = i*y_ratio
            temp.append(points[(y2*w1)+x2])
                                   
    return temp


def convert(picture, compression, nb_means, output):
    # Load the picture
    img = Image.open(picture)
    height = img.height
    width = img.width

    # Get list of points (pixel value)
    points = []
    for y in range(img.height):
        for x in range(img.width):
            points.append(img.getpixel((x, y)))

    # Re-scale picture
    if compression > 0:
        width = int(img.width*(100-compression)/100)
        height = int(img.height*(100-compression)/100)
        points = nearest_neighbor(points, img.width, img.height, width, height)

    # Create the centroids
    centroids = kmeans(points, nb_means)

    # For each centroid bind an ascii value
    table = [ string.punctuation[i] for i in range(nb_means) ]
    
    # Determine for each pixel the centroid value
    def nearest(centroids, point):
        distances = [] 
        for centroid in centroids:
            distances.append(((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2 + + (centroid[2]-point[2])**2)**(1/2))

        return centroids[distances.index(min(distances))]

    txt = []
    for y in range(height):
        txt.append([])
        for x in range(width):
            txt[y].append(table[centroids.index(nearest(centroids, points[y*width+x]))])

    # Print in a file
    if output:
        with open(output, 'w') as file:
            for line in txt:
                file.write(''.join(line) + '\n')
    else:
        for line in txt:
            print(''.join(line))


def main():
    parser = argparse.ArgumentParser(prog = 'ASCII art converter',
                    description = 'ASCII art converter based on K-Means algorithm')

    parser.add_argument('picture')
    parser.add_argument('-g', '--nb_group', type=int, default=20) 
    parser.add_argument('-c', '--compression', type=int, default=0) 
    parser.add_argument('-o', '--output', default=None) 

    args = parser.parse_args()

    if args.nb_group > 31 or args.nb_group <= 0:
        raise ValueError('Nb group must be greater than 0 and lesser than 31')
    if args.compression > 90 or args.compression < 0:
        raise ValueError('Compression only between 0-90%')

    convert(args.picture, args.compression, args.nb_group, args.output)


if __name__ == '__main__':
    main()