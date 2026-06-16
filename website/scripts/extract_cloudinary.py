import re,glob
p=re.compile(r'https?://res.cloudinary.com[^"'"'\s<>)]+')
urls=set()
for fp in glob.glob('**/*.html', recursive=True):
    try:
        with open(fp,encoding='utf-8') as f:
            urls.update(p.findall(f.read()))
    except Exception as e:
        print('ERR',fp,e)
urls=sorted(urls)
with open('cloudinary_urls.txt','w',encoding='utf-8') as out:
    out.write('\n'.join(urls))
for u in urls:
    print(u)
