import cv2
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

#Đọc dữ liệu nhãn
def read_labels(file_path):
    """
    Đọc dữ liệu nhãn từ file csv

    :param file_path: Đường dẫn đến file nhãn
    :return: Danh sách các nhãn
    """
    labels = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            labels.append(int(row[0]))
    return labels

#Lấy danh sách ảnh trong thư mục
def get_image_paths(folder_path):
    """
    Lấy danh sách các đường dẫn ảnh trong thư mục

    :param folder_path: Đường dẫn đến thư mục chứa ảnh
    :return: Danh sách các đường dẫn ảnh
    """
    image_files = os.listdir(folder_path)
    image_paths = []
    for filename in image_files:
       image_paths.append(os.path.join(folder_path, filename))
    return sorted(image_paths)

# Tải và xử lý một ảnh
def load_and_process_image(image_path):
    """
    Tải và xử lý một ảnh

    :param image_path: Đường dẫn đến ảnh
    :return: Ảnh đã được xử lý
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return image

# Tải và xử lý bộ dữ liệu ảnh
def load_and_process_images(image_paths):
    """
    Tải và xử lý bộ dữ liệu ảnh

    :param image_paths: Danh sách các đường dẫn ảnh
    :return: Ma trận chứa các ảnh đã được xử lý
    """
    images = []
    for path in image_paths:
        images.append(load_and_process_image(path))  # Chuyển đổi ảnh thành vector
    return np.array(images)

# Khởi tạo dữ liệu
train_images_path = os.path.join('data', 'FashionMNIST', 'images', 'train-images')
test_labels_path = os.path.join('data', 'FashionMNIST', 'labels', 'train-labels.csv')

x_train_images = load_and_process_images(get_image_paths(train_images_path))
y_train = np.array(read_labels(test_labels_path))

fashion_mnist_labels = {
    0: 'T-shirt/top',
    1: 'Trouser',
    2: 'Pullover',
    3: 'Dress',
    4: 'Coat',
    5: 'Sandal',
    6: 'Shirt',
    7: 'Sneaker',
    8: 'Bag',
    9: 'Ankle boot'
}

# Sử dụng PCA để giảm số chiều xuống 2
x_train_images_flat = x_train_images.reshape(len(x_train_images), -1)
pca = PCA(n_components=2)
x_train_images_pca = pca.fit_transform(x_train_images_flat)

#Vẽ biểu đồ phân bố dữ liệu trên không gian 2 chiều
# Biểu đồ hiển thị phân bố các mẫu kiểm thử trên không gian PCA 2D theo nhãn thật
plt.figure(figsize=(8, 6))

#Tạo bảng màu cho các lớp
colors = plt.cm.rainbow(np.linspace(0, 1, len(np.unique(y_train))))

# Vẽ từng lớp

for label, color in zip(np.unique(y_train), colors):
    mask = y_train == label
    plt.scatter(x_train_images_pca[mask, 0], x_train_images_pca[mask, 1], 
                color=color, label=f"{fashion_mnist_labels[label]}")

plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('PCA of Fashion MNIST Dataset')
plt.legend()
plt.show()