#!/usr/bin/python

import data_reader_initializer
import gzip
import os
import re
import tag_manager

from functools import lru_cache

class file_system_reader(data_reader_initializer.data_reader):

    DATA_FOLDER_NAME = "data"
    TAG_FOLDER_NAME = "tags"
    TRANSLATION_FOLDER_NAME = "translate"
    TRANSLATION_FILE_PREFIX = "__translate__"
    ROOT_DIR_PROPERTY = 'rootdir'
    COMPRESSION_PROPERTY = 'compression'
    root_dir = ''
    root_dir_norm = None
    object_id_pattern = re.compile(r'(?P<fileid>\d+):(?P<index>\d+)')
    
    def __init__(self, param_dict):
        assert (self.ROOT_DIR_PROPERTY in param_dict), "Expected property not present in params passed."
        self.root_dir = param_dict[self.ROOT_DIR_PROPERTY]
        self.create_folders()

    def create_folders(self):
        self.root_dir_norm = os.path.normpath(self.root_dir)

        if not os.path.exists(os.path.join(self.root_dir_norm, self.DATA_FOLDER_NAME)):
            os.mkdir(os.path.join(self.root_dir_norm, self.DATA_FOLDER_NAME))

        if not os.path.exists(os.path.join(self.root_dir_norm, self.TRANSLATION_FOLDER_NAME)):
            os.mkdir(os.path.join(self.root_dir_norm, self.TRANSLATION_FOLDER_NAME))

        if not os.path.exists(os.path.join(self.root_dir_norm, self.TAG_FOLDER_NAME)):
            os.mkdir(os.path.join(self.root_dir_norm, self.TAG_FOLDER_NAME))

    def get_object(self, id):
        file_name = self.get_object_impl(id)
        file_data = self.retrieve_data(file_name)

    @lru_cache(maxsize = 1024)
    def get_object_id_list_for_tag(self, tag_expression):
        tag_finder = tag_manager.tag_manager(tag_expression, self)

        return tag_finder.parse()

    def get_object_id_list_for_full_text(self, full_text):
        print("get_object called")

    def assert_folder_exists(self, folder_name):
        assert(os.path.exists(os.path.join(self.root_dir_norm, folder_name))), "folder does not exist"
        
    @lru_cache(maxsize = 1024)
    def get_object_impl(self, id):
        self.assert_folder_exists(self.TRANSLATION_FOLDER_NAME)
        object_id_pattern_match = self.object_id_pattern.match(id)
        assert(object_id_pattern_match), "Invalid id object, does not match the expected pattern";
        file_suffix = object_id_pattern_match.group('fileid')
        index_in_file = object_id_pattern_match.group('index')
        file_list = []
        with open(os.path.join(self.root_dir_norm, self.TRANSLATION_FOLDER_NAME, self.TRANSLATION_FILE_PREFIX + file_suffix), 'r') as translation_file:
            file_list.extend(translation_file.read().splitlines())

        return file_list[int(index_in_file)]

    @lru_cache(maxsize = 1024)
    def retrieve_data(self, file_name):
        self.assert_folder_exists(self.DATA_FOLDER_NAME)
        with gzip.open(os.path.join(self.root_dir_norm, self.DATA_FOLDER_NAME, file_name), mode = 'rb') as gzipped_data_file:
            file_data = gzipped_data_file.read()
            return file_data.decode('utf-8')

    @lru_cache(maxsize = 1024)
    def get_tag_data(self, tag_name):
        self.assert_folder_exists(self.TAG_FOLDER_NAME)
        with open(os.path.join(self.root_dir_norm, self.TAG_FOLDER_NAME, tag_name), 'r') as tag_file:
            return set(tag_file.read().splitlines())

    def clear_tag_cache(self):
        self.get_tag_data.cache_clear()
        self.get_object_id_list_for_tag.cache_clear()
