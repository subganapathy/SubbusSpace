#!/usr/bin/python

import glob

from configparser import ConfigParser
import file_system_reader

class data_reader_initializer:
    CFG_GLOB = '*.cfg'
    DEFAULT_BLOCK = 'Global'
    PREFERRED_KEY = 'Preferred'
    SUPPORTED_STRUCTURES = ['Filesystem']
    param_dict = {}
    preferred = ''
    def __init__(self):
        cfg_files = glob.glob(self.CFG_GLOB)
        cfg_file = cfg_files.pop()

        config_parser = ConfigParser()
        config_parser.read(cfg_file)

        self.preferred = config_parser[self.DEFAULT_BLOCK][self.PREFERRED_KEY]
        self.param_dict = dict(config_parser.items(self.preferred))
        
    def get_data_reader(self):
        assert (self.preferred in self.SUPPORTED_STRUCTURES), "An unsupported entity is marked as preferred!"
        
        return file_system_reader.file_system_reader(self.param_dict)


class data_reader:

    def get_object(self, id):
        raise NotImplementedError()

    def get_object_id_list_for_tag(self, tag_name):
        raise NotImplementedError()

    def get_object_id_list_for_full_text(self, full_text):
        raise NotImplementedError()


if __name__ == "__main__":
    foo = data_reader_initializer()
    bar = foo.get_data_reader()
    output = bar.get_object('1:2')
    print(output)
