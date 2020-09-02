import scrapy
import json
class DrugSpider(scrapy.Spider):
    
    with open('D:\gdirve\PKU\drugs\drug_hrefs.json','r',encoding='utf8') as f:
        hrefs = json.load(f)

    href_all = []
    for drug, company in hrefs.items():
        links = list(company.values())
        href_all.append(links)
    
    def flat(a):
        return [item for sublist in a for item in sublist]
    
    href_all = flat(href_all)

    name = 'drugs'
    
    #start_urls = ['https://www.yaopinnet.com/huayao/hy22936.htm']
    start_urls = href_all
    def parse(self,response):
        react_dict = {}

        drug_name = ''.join(response.css('h1[class="yaopinming"]::text').extract())

        company = ''.join(response.css('a[class="qiye"]::text').extract())

        drug_with_company = (drug_name,company)

        link = response.url

        react = ''.join(response.css('li[class="smsli"]:contains("不良反应")::text').extract())
        react_dict[drug_name] = react

        company_name = '%s.txt' % company
        filename = '说明书_2\\' +drug_name +'.txt' #+ '_' + company_name

        with open(filename,'w',encoding='utf8') as f:
            f.write('drug_name:{}company:{}react:{}link:{}'.format(drug_name,company,react,link))
            


        # with open('drugs_yaopin.json','w',encoding='utf8') as jfile:
        #     json.dump(react_dict,jfile,ensure_ascii=False)

