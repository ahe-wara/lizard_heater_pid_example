class Data_Logger:

        def __init__(self, file_name):
            self.__file_name = file_name
            self.__file = open(str(file_name), "w")

        def write_to_logger(self, string_to_write):          
            self.__file.write(string_to_write) + "\n")
            self.__file.flush()
                       
        def close_logger(self):          
            file.write(string_to_write)
            
        def print_logger(self):          
            print(file.read)
            