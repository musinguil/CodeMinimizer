import os

def main():
    minimizeCode()

def minimizeCode():
    for path in getFiles():
        if len(path.split('.')) >= 2:
            if path.split('.')[1] == 'css' or path.split('.')[1] == 'js' or path.split('.')[1]== 'html':
                print('Minimizing' + path)
                current_file = open(path, 'r')
                content = current_file.read()
                content = content.replace('\n', '')
                current_file.close()
                current_file = open(path, 'w')
                current_file.write(content.replace('\t', ''))
    
    print('Minimizing index.html')
    current_file = open('index.html', 'r')
    content = current_file.read()
    content = content.replace('\n', '')
    current_file.close()
    current_file = open('index.html', 'w')
    current_file.write(content.replace('\t', ''))
    

def getFiles():
    folders = []
    for r, d, f in os.walk('.\\'):
        for folder in d:
            path = os.getcwd() + os.path.join(r, folder)[1:]
            for file in os.listdir(path):
                folders.append(path + '\\' + file)
    return folders

if __name__ == "__main__":
    minimizeCode()