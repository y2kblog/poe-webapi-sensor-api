#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import glob

# Third party libraries
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
from gfm import AutolinkExtension, TaskListExtension


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
    <link rel="stylesheet" href="/docs/api/tools/openapi-generator/html-style/prism.css">
    <title>HTML_TITLE</title>
</head>
<body>
<script type="text/javascript" src="/docs/api/tools/openapi-generator/html-style/prism.js"></script>
<article class="markdown-body">
"""
FOOT_STR = """
</article>
</body>
</html>
"""


def main():
    ext = [GithubFlavoredMarkdownExtension()]
    # ext = [AutolinkExtension(), TaskListExtension(max_depth=2)]
    md = markdown.Markdown(extensions=ext)
    mdPathList = glob.glob(os.path.dirname(os.path.abspath(sys.argv[0])) + '/**/*.md', recursive=True)
    # print(mdPathList)
    for mdPath in mdPathList:
        if 'venv' in mdPath:
            continue
        print(mdPath)
        file_name = os.path.splitext(os.path.basename(mdPath))[0]
        # print(file_name)
        output = [HEAD_STR.replace('HTML_TITLE', file_name)]
        with open(mdPath, mode='r', encoding='utf-8') as f:
            s = f.read()
            html_body = md.convert(s)
        html_body = html_body.replace('.md', '.html')
        output.append(html_body)
        output.append(FOOT_STR)
        # print(output)
        
        # with open('./html/' + file_name + '.html', mode='w', encoding='utf-8') as f:
        with open(os.path.join(os.path.dirname(mdPath), file_name + '.html'), mode='w', encoding='utf-8') as f:
            f.write(''.join(output))
            # f.write(html_body)
        # print(md.convert(sample_text))


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    main()
