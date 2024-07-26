import sys
import markdown


def convert_html(inputfile, outputfile):
    with open(inputfile, 'r') as f:
        contents = f.read()
    
    md = markdown.Markdown(extensions=['extra', 'fenced_code', 'codehilite', 'tables', 'sane_lists'])
    html = md.convert(contents)
    
    with open(outputfile, 'w') as f:
        f.write(html)


if __name__ == "__main__":
    if sys.argv[1] == "markdown":
        inputfile = sys.argv[2]
        outputfile = sys.argv[3]
        convert_html(inputfile, outputfile)

