#!/usr/bin/python

import os
import data_reader_initializer

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
        print("get_object called")

    def get_object_id_list_for_tag(self, tag_name):
        print("get_object called")

    def get_object_id_list_for_full_text(self, full_text):
        print("get_object called")

    def assert_folder_exists(self, folder_name):
        assert(os.path.exists(os.path.join(self.root_dir_norm, folder_name))), "folder does not exist"
        
    @lru_cache(maxsize = 1024)
    def get_object_impl(self, id):
        assert_folder_exists(TRANSLATION_FOLDER_NAME)
        
               
        
