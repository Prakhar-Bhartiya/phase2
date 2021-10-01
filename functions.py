
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2   
import matplotlib
from scipy.stats import skew, kurtosis
from skimage.feature import hog
from skimage import exposure
from skimage import io
import numpy as np
import cv2
import json
import os
import warnings

warnings.filterwarnings('ignore')

class Reductions:
    max=100
    def __init__(self, k=2, tolerance=0.001):
        self.k = k
        self.tolerance = tolerance

    def get_kmeans(self, data):

        self.kmeans = {}

        for i in range(self.k):
            self.kmeans[i] = data[i]

        for i in range(self.max):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset-self.kmeans[kmean]) for kmean in self.kmeans]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_kmeans = dict(self.kmeans)

            for classification in self.classifications:
                self.kmeans[classification] = np.average(self.classifications[classification],axis=0)

            optimized = True

            for c in self.kmeans:
                original_kmean = prev_kmeans[c]
                current_kmean = self.kmeans[c]
                if np.sum((current_kmean-original_kmean)/original_kmean*100.0) > self.tolerance:
                    print(np.sum((current_kmean-original_kmean)/original_kmean*100.0))
                    optimized = False

            if optimized:
                print("\n[OPTIMIZED]")
                break

        
# NEW PYHTON
def process_t1(images):

    reduction_tech = Reductions()
    for i in range(3):

        # d_img_name = './temp/gtm_temp_{}_.png'.format(i)
        # matplotlib.image.imsave(d_img_name, images[i], cmap="gray")
        reduction_tech.get_kmeans(images[i])
        print("\n [i]:[{}]".format(reduction_tech.kmeans))


        


    


