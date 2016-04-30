
##### brute force scraping
import scrapy
from comic.items import ComicItem
from comic.items import TableItem


class ComicsalesSpider(scrapy.Spider):
    name = "salestable"
    allowed_domains = ["http://www.comichron.com"]
    start_urls = [
    'http://www.comichron.com/monthlycomicssales/1995/1995-01Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-02Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-03Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-04Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-05Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-06Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-07Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-08Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-09Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-10Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-11Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1995/1995-12Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-01Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-02Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-03Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-04Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-05Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-06Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-07Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-08Diamond.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-09.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-10.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-11.html',
    'http://www.comichron.com/monthlycomicssales/1996/1996-12.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-01.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-02.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-03.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-05.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-06.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-09.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-04.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-05.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-06.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-07.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-08.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-09.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-10.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-11.html',
    'http://www.comichron.com/monthlycomicssales/1997/1997-12.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-01.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-02.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-03.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-04.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-05.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-06.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-07.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-08.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-09.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-10.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-11.html',
    'http://www.comichron.com/monthlycomicssales/1998/1998-12.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-01.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-02.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-03.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-04.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-05.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-06.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-07.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-08.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-09.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-10.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-11.html',
    'http://www.comichron.com/monthlycomicssales/1999/1999-12.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-01.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-02.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-03.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-04.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-05.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-06.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-07.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-08.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-09.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-10.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-11.html',
    'http://www.comichron.com/monthlycomicssales/2000/2000-12.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-01.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-02.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-03.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-04.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-05.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-06.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-07.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-08.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-09.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-10.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-11.html',
    'http://www.comichron.com/monthlycomicssales/2001/2001-12.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-01.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-02.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-03.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-04.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-05.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-06.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-07.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-08.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-09.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-10.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-11.html',
    'http://www.comichron.com/monthlycomicssales/2002/2002-12.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-01.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-02.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-03.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-04.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-05.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-06.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-07.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-08.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-09.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-10.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-11.html',
    'http://www.comichron.com/monthlycomicssales/2003/2003-12.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-01.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-02.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-03.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-04.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-05.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-06.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-07.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-08.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-09.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-10.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-11.html',
    'http://www.comichron.com/monthlycomicssales/2004/2004-12.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-01.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-02.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-03.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-04.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-05.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-06.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-07.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-08.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-09.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-10.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-11.html',
    'http://www.comichron.com/monthlycomicssales/2005/2005-12.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-01.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-02.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-03.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-04.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-05.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-06.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-07.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-08.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-09.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-10.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-11.html',
    'http://www.comichron.com/monthlycomicssales/2006/2006-12.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-01.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-02.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-03.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-04.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-05.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-06.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-07.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-08.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-09.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-10.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-11.html',
    'http://www.comichron.com/monthlycomicssales/2007/2007-12.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-01.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-02.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-03.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-04.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-05.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-06.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-07.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-08.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-09.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-10.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-11.html',
    'http://www.comichron.com/monthlycomicssales/2008/2008-12.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-01.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-02.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-03.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-04.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-05.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-06.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-07.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-08.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-09.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-10.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-11.html',
    'http://www.comichron.com/monthlycomicssales/2009/2009-12.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-01.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-02.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-03.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-04.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-05.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-06.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-07.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-08.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-09.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-10.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-11.html',
    'http://www.comichron.com/monthlycomicssales/2010/2010-12.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-01.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-02.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-03.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-04.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-05.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-06.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-07.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-08.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-09.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-10.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-11.html',
    'http://www.comichron.com/monthlycomicssales/2011/2011-12.html'
        ]

    def parse(self, response):
        date=response.xpath("//div[@id='content']/div[2]/div[4]/big[1]/big/span/big/big/text()").extract()
        for sel in response.xpath("//table[@width='660']/tbody/tr[contains(td[2], 'Trade Paperback')]/preceding-sibling::tr[not (@class='x168')]"):
            if (sel.xpath("td[1]/text()").extract())[0]!="\n" and (sel.xpath("td[5]/text()").extract())[0]=="Marvel":
                item = TableItem()
                item['date'] = date
                item['rank'] = sel.xpath("td[1]/text()").extract()
                item['title'] = sel.xpath("td[2]/text()").extract()
                item['issue']=sel.xpath("td[3]/text()").extract()
                item['price']=sel.xpath("td[4]/text()").extract()
                item['publisher']=sel.xpath("td[5]/text()").extract()
                item['orders']=sel.xpath("td[6]/text()").extract()
                yield item
