
from string import Template

def main():
    
    # create a template with placeholders
    templ = Template("With title: ${title} by author ${author}")

    # use the substitute method with a dictionary
    data = { 
        "author": "John Doe",
        "title": "Python"
    }

    str3 = templ.substitute(data)    
    print(str3)

    data2 = { 
        "author": "Martin Doe",
        "title": "Java"
    }

    datalist = {1: data, 2: data2}

    for key, value in datalist.items():
        out = templ.substitute(value)
        print(out)

if __name__ == "__main__":
    main()
    