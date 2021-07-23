import requests

def save_file_from_www(link):
    filename = link.split('/')[-1]
    r = requests.get(link, allow_redirects=True)
    open(filename, 'wb').write(r.content)


link1 = 'https://webservices.mirea.ru/upload/iblock/a68/012ubowp6mcz42zrang4sazxpjrxi7ly/%D0%97%D0%B0%D1%87_%D0%98%D0%9A%D0%B8%D0%B1_1%D0%BA_20-21_%D0%BB%D0%B5%D1%82%D0%BE.xlsx'
link2 = 'https://webservices.mirea.ru/upload/iblock/315/mquktq1f5c3uyemgccqrr63vz3d22er9/%D0%97%D0%B0%D1%87_%D0%98%D0%9A%D0%B8%D0%B1_2%D0%BA_20-21_%D0%BB%D0%B5%D1%82%D0%BE.xlsx'
link3 = 'https://webservices.mirea.ru/upload/iblock/19f/irxe7ayvzvkrnrq32hogt1ccnj3wywi4/%D0%97%D0%B0%D1%87_%D0%98%D0%9A%D0%B8%D0%B1_3%D0%BA_20-21_%D0%BB%D0%B5%D1%82%D0%BE.xlsx'
link4 = 'https://webservices.mirea.ru/upload/iblock/a12/vkqiteb23sogk3ex328816v3hsol913n/%D0%97%D0%B0%D1%87_%D0%98%D0%9A%D0%B8%D0%B1_4%D0%BA_20-21_%D0%BB%D0%B5%D1%82%D0%BE.xlsx'
link5 = 'https://webservices.mirea.ru/upload/iblock/8f7/sa1pvfbc311i1jps65ekvv8833smr038/%D0%97%D0%B0%D1%87_%D0%98%D0%9A%D0%B8%D0%B1_5%D0%BA_20-21_%D0%BB%D0%B5%D1%82%D0%BE.xlsx'
link6 = 'https://webservices.mirea.ru/upload/iblock/4c1/7qm8pooo0i9djs4aum9qb9waim68b87s/%D0%98%D0%9A_1%D0%BA_20-21_%D0%B2%D0%B5%D1%81%D0%BD%D0%B0.xlsx'
link7 = 'https://webservices.mirea.ru/upload/iblock/f99/cxjclwr9wh2dr0w3pclwj1bqbrcj0nsa/%D0%98%D0%9A_2%D0%BA_20-21_%D0%B2%D0%B5%D1%81%D0%BD%D0%B0.xlsx'
link8 = 'https://webservices.mirea.ru/upload/iblock/7e6/lbp6v0xizziezece3cqw2tb44jb5v07t/%D0%98%D0%9A_3%D0%BA_20-21_%D0%B2%D0%B5%D1%81%D0%BD%D0%B0.xlsx'
link9 = 'https://webservices.mirea.ru/upload/iblock/d9b/0ibbgtavz4t4e4vid13yq3m1ba16dh5e/%D0%98%D0%9A_4%D0%BA_20-21_%D0%B2%D0%B5%D1%81%D0%BD%D0%B0_9-17%D0%BD..xlsx'
link10 = 'https://webservices.mirea.ru/upload/iblock/a67/xr9lo4j2itlp183vsi3q7d6gcx0497vo/%D0%98%D0%9A_5%D0%BA_20-21_%D0%B2%D0%B5%D1%81%D0%BD%D0%B0.xlsx'
link11 = 'https://webservices.mirea.ru/upload/iblock/b44/5bukbbggsst8osgktsyhljb8s5h1ayf3/%D0%AD%D0%BA%D0%B7_%D0%98%D0%9A%D0%B8%D0%B1_1%D0%BA_20-21_%D0%BB%D0%B5%D1%82%D0%BE.xlsx'
link12 = 'https://webservices.mirea.ru/upload/iblock/d84/r5bzo02sgkcgzjcq7lb0yshl91nto0fu/%D0%AD%D0%BA%D0%B7_%D0%98%D0%9A%D0%B8%D0%B1_2%D0%BA_20-21_%D0%BB%D0%B5%D1%82%D0%BE.xlsx'
link13 = 'https://webservices.mirea.ru/upload/iblock/47d/tunxachs2aj9gtznnrs3fr2ya8vlt5vv/%D0%AD%D0%BA%D0%B7_%D0%98%D0%9A%D0%B8%D0%B1_3%D0%BA_20-21_%D0%BB%D0%B5%D1%82%D0%BE.xlsx'
link14 = 'https://webservices.mirea.ru/upload/iblock/2ec/517ld4d5r2xvdamlujez6q0vz9dck4tm/%D0%AD%D0%BA%D0%B7_%D0%98%D0%9A%D0%B8%D0%B1_4%D0%BA_20-21_%D0%BB%D0%B5%D1%82%D0%BE.xlsx'
link15 = 'https://webservices.mirea.ru/upload/iblock/e98/vnd1hkcbxlmos55nkbu6y1519ojltk1h/%D0%AD%D0%BA%D0%B7_%D0%98%D0%9A%D0%B8%D0%B1_5%D0%BA_20-21_%D0%BB%D0%B5%D1%82%D0%BE.xlsx'
links = [link1, link2, link3, link4, link5, link6, link7, link8, link9, link10, link11, link12, link13, link14, link15]

i = 0
for i in links:
    save_file_from_www(i)
