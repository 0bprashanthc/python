def get_links(html):
    out = open("links.txt","a")
    html = open(html).read()
    while html.find('http') != -1:
        import pdb; pdb.set_trace();
        start = html.find('href="http')
        target = html.find('http',start+1)
        end = html.find('/>',target+1)
        print html[target:end]
        """
        out.write(html[target:end])
        out.write("\n")
        html = html[end+1:]
        """
        break

if __name__ == "__main__":
    get_links("index.htm")
