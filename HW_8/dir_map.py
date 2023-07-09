# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# - Для дочерних объектов указывайте родительскую директорию.
# - Для каждого объекта укажите файл это или директория.
# - Для файлов: сохраните его размер в байтах,
#   а для директорий: размер файлов в ней с учётом всех вложенных файлов и директорий.

import os
import csv
import json
import pickle

def dir_size(dir):
    size = 0
    for dir_path, dir_name, file_name in os.walk(dir):
        for f in file_name:
            fp = os.path.join(dir_path, f)
            size += os.path.getsize(fp)
    return size


def dir_map_dict(dir):
    dir_map = {}
    
    for dir_path, dir_name, file_name in os.walk(dir):
        dir_map[f"DIR - {dir_path} / {dir_size(dir_path)} bytes"] = [f"File - {i} / {os.path.getsize(os.path.abspath(dir_path + '/' + i))} bytes" for i in file_name]
    return dir_map

def to_csv(dir_dict):
    data = [["DIR", "Files"]]
    
    for key, value in dir_dict.items():
        data.append([key, value])
    with open("csv_map.csv", "w", encoding="utf-8") as csv_f:
        write_csv = csv.writer(csv_f, dialect="excel-tab", delimiter=",")
        write_csv.writerows(data)
        
def to_json(dir_dict):    
    with open("json_map.json", "w", encoding="utf-8") as json_f:
        json.dump(dir_dict, json_f, indent=2, separators=(",", ":"))


def to_pickle(dir_dict):
    with open("pickle_map.bin", "wb") as pickle_f:
        pickle.dump(dir_dict, pickle_f)


dir = "tree_dir"
dir_map = dir_map_dict(dir)
to_csv(dir_map)
to_json(dir_map)
to_pickle(dir_map)
print(dir_size(dir), 'bytes')