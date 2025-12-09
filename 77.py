import requests


class MyFile:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def Error(self, name_of_error):
        print(name_of_error)
        exit()

    def check_mode(self, mode):
        if self.mode != mode:
            self.Error('Выбранный режим не позволяет выполнить данную функцию')

    def read(self):
        self.check_mode('read')
            
        with open(self.name, 'r', encoding='UTF-8') as file:
            return file.read()
    
    def write(self, string):
        if self.mode == 'write':
            with open(self.name, 'w', encoding='UTF-8') as file:
                file.write(string)
        elif self.mode == 'append':
            with open(self.name, 'a', encoding='UTF-8') as file:
                file.write(string)
        else:
            self.Error('Выбранный режим не позволяет выполнить данную функцию')
        
    def read_url(self):
        self.check_mode('url')
        try:
            return requests.get(self.name).text
        except:
            self.Error('Такой ссылки не существует')

    def count_urls(self):
        self.check_mode('url')

        string = self.read_url()
        bad_chars = [' ', '<', '>', '\n', '\t', '"', "'"]
        answer = 0
        i = 0
        while i < len(string):
            if string[i:i+4] != 'http':
                i += 1
                continue
            if string[i+4:i+7] == '://' or string[i+4:i+8] == 's://':
                answer += 1
                #old_i = i
                while i < len(string) and string[i] not in bad_chars:
                    i += 1
                #cur_url = string[old_i:i]
                #print(cur_url)
            else:
                i += 1
        return answer
        
    def write_url(self, name):
        self.check_mode('url')
        
        with open(name, 'w', encoding='UTF-8') as file:
            file.write(self.read_url())
