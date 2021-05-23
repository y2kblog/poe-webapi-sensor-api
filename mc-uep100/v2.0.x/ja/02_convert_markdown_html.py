#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import glob
import pathlib

# Third party libraries
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension


HEAD_STR = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/4.0.0/github-markdown.min.css">
    <style>
        .markdown-body {
            box-sizing: border-box;
            min-width: 200px;
            max-width: 980px;
            margin: 0 auto;
            padding: 45px;
        }
        @media (max-width: 767px) {
            .markdown-body {
                padding: 15px;
            }
        }
    </style>
    <link rel="stylesheet" href="https://rawgithub.com/y2kblog/poe-webapi-sensor-api/master/tools/openapi-generator/html-style/prism.css">
    <title>HTML_TITLE</title>
</head>
<body>
<script type="text/javascript" src="https://rawgithub.com/y2kblog/poe-webapi-sensor-api/master/tools/openapi-generator/html-style/prism.js"></script>
<article class="markdown-body">
"""
FOOT_STR = """
</article>
</body>
</html>
"""


def main():
    md = markdown.Markdown(extensions=[GithubFlavoredMarkdownExtension()])
    mdPathList = glob.glob(os.path.dirname(os.path.abspath(sys.argv[0])) + '/**/*.md', recursive=True)
    for mdPath in mdPathList:
        if 'venv' in mdPath:
            continue
        print(mdPath)
        # sys.exit()

        file_name = os.path.splitext(os.path.basename(mdPath))[0]
        # print(file_name)
        output = [HEAD_STR.replace('HTML_TITLE', file_name)]
        s = ''
        with open(mdPath, mode='r', encoding='utf-8') as f:
            s = f.read()
        if 'python' in os.path.dirname(mdPath):
            p = pathlib.Path(os.path.dirname(os.path.abspath(sys.argv[0])))
            project_name = f'{p.parts[-3].upper()}-python'
            src_str = r'git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git'
            dst_str = r'"git+https://github.com/y2kblog/poe-webapi-sensor-api.git'\
                    + f"#egg={project_name}&subdirectory="\
                    + f"{'/'.join(p.parts[-3:])}/autogen-openapi-generator/python\""
            # print(dst_str)
            s = s.replace(src_str, dst_str)
        try:
            with open(mdPath, mode='w', encoding='utf-8') as f:
                f.write(s)
        except Exception as e:
            print(e)
        html_body = md.convert(s)
        html_body = html_body.replace('.md', '.html')
        output.append(html_body)
        output.append(FOOT_STR)
        # print(output)

        with open(os.path.join(os.path.dirname(mdPath), file_name + '.html'), mode='w', encoding='utf-8') as f:
            f.write(''.join(output))


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    main()
