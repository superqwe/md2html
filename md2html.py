# 03.06.17

# TODO fix codice multiriga
# TODO creare css
# TODO multiprocesso

import os

from pprint import pprint as pp
import markdown

PATH_SOURCE = 'TypeScript-Handbook'
PATH_DESTINATION = 'html'


def main():
    base_path = os.path.split(os.path.realpath(__file__))[0]

    path_root = os.path.join(base_path, PATH_SOURCE)

    for root, dirs, files in os.walk(path_root):
        f_md = [f for f in files if os.path.splitext(f)[1] == '.md']

        if f_md:
            fin = [os.path.join(root, f) for f in f_md]
            dir_html = root.replace(PATH_SOURCE, PATH_DESTINATION)

            if not os.path.exists(dir_html):
                print('creazione ', dir_html)
                os.makedirs(dir_html, exist_ok=True)

            for f in fin:
                fout = f.replace(PATH_SOURCE, PATH_DESTINATION)
                fout = fout.replace('.md', '.html')


                print(f, fout, sep='\n', end='\n\n')

                markdown.markdownFromFile(f, fout)


if __name__ == '__main__':
    main()
