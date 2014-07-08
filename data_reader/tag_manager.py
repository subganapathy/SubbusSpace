#!/usr/bin/python

import data_reader_initializer.data_reader_initializer
import io
import shlex

class tag_manager:

    current_data_reader = None
    lexer = None
    global_set = None
    GLOBAL_TAG_FILE = '__global__'

    def __init__(self, tag_expression, data_reader):
        self.lexer = shlex.shlex(instream = io.StringIO(tag_expression))
        self.current_data_reader = data_reader
        global_set = data_reader.get_tag_data(self.GLOBAL_TAG_FILE)
    
    def parse(self):
        return self.or_expression()

    def or_expression(self):
        result_set = self.and_expression()
        while lexer.get_token() == '|':
            rhs_set = self.and_expression()
            result_set |= rhs_set

        return result_set

    def and_expression(self):
        result_set = self.token_not_expression()
        while lexer.get_token() == '^':
            rhs_set = self.token_not_expression()
            result_set &= rhs_set

        return result_set

    def token_not_expression(self):
        token = lexer.get_token()

        if token == '~':
            return self.global_set - self.token_not_expression()

        token = lexer.get_token()
        return self.current_data_reader.get_tag_data(token)
        
