import gzip
import idx2numpy
import csv
import os 
from PIL import Image

def save_image(image_data, image_path):
    """
    Lưu ảnh vào thư mục

    :param image_data: Dữ liệu ảnh
    :param image_path: Đường dẫn lưu ảnh
    """
    image = Image.fromarray(image_data)
    image.save(image_path)

def extract_images(file_path, output_folder):
    """
    Giải nén và lưu ảnh từ file .gz

    :param file_path: Đường dẫn đã được nén
    :param output_folder: Đường dẫn lưu thư mục các ảnh sau khi giải nén
    """
    
    # Tải dữ liệu từ file nén
    images_data = idx2numpy.convert_from_file(file_path)

    #Kiểm tra xem thư mục đã tồn tại chưa để tạo mới
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

        # Lặp qua bộ dữ liệu ảnh và lưu từng ảnh vào thư mục
    for i, image in enumerate(images_data):
        image_path = os.path.join(output_folder, '{:05d}.png'.format(i))
        save_image(image, image_path)

def extract_labels(file_path, output_folder, output_file):
    """
    Giải nén và lưu thông tin nhãn dữ liệu vào tập tin csv

    :param file_path: Đường dẫn đã được nén
    :param output_folder: Đường dẫn lưu thư mục các nhãn sau khi giải nén
    :param output_file: Đường dẫn lưu file nhãn
    """

    # Kiểm tra xem thư mục đã tồn tại chưa để tạo mới
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Đọc dữ liệu nhãn từ file nén
    label_data = idx2numpy.convert_from_file(file_path)

    #lưu vào tập tin csv
    csv_file = os.path.join(output_folder, output_file)

    # Mở tập tin csv để ghi
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Ghi dữ liệu và tập tin csv
        for label in label_data:
            writer.writerow([label])

# Thông tin thư mục
source_folder = os.path.join('data', 'FashionMNIST','raw')
images_destination_folder = os.path.join('data', 'FashionMNIST','images')
labels_destination_folder = os.path.join('data', 'FashionMNIST','labels')

# Liệt kê các file nén trong thư mục
file_list = os.listdir(source_folder)

#Lặp qua danh sách các file nén
for file_name in file_list:
    # Tạo đường dẫn đầy đủ cho tập tin hoặc thư mục.
    source_fille = os.path.join(source_folder, file_name)
    
    # Kiểm tra có phải file không
    if os.path.isfile(source_fille):
        # Kiểm tra xem file có phải là file ảnh không
        if file_name.endswith('.gz'):
            output_file_path = os.path.join(source_folder, file_name[0:len(file_name)-len(".gz")])
            with gzip.open(source_fille, 'rb') as f_in:  # sửa source_file thành source_fille
                with open(output_file_path, 'wb') as f_out:
                    f_out.write(f_in.read())

file_list = os.listdir(source_folder)
# Lặp qua danh sách các file nén
for file_name in file_list:
    # Tạo đường dẫn đầy đủ cho tập tin hoặc thư mục.
    source_file = os.path.join(source_folder, file_name)
    # Kiểm tra có phải file không
    if os.path.isfile(source_file):
        # Kiểm tra xem file có đuôi -idx1-ubyte không thì đây là file nhãn
        if file_name.endswith('-idx1-ubyte'):
            # Giải nén và lưu các nhãn
            extract_labels(source_file, labels_destination_folder, file_name[0:len(file_name)-len("-idx1-ubyte")]+'.csv')
        elif file_name.endswith('-idx3-ubyte'):
            # Giải nén và lưu các ảnh
            destination_sub_folder = os.path.join(images_destination_folder, file_name[0:len(file_name)-len("-idx3-ubyte")])
            extract_images(source_file, destination_sub_folder)
            print(f"Đã giải nén và lưu ảnh từ {file_name} vào {destination_sub_folder}")