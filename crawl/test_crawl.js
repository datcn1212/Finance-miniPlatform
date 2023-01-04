const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

const getHTML  = async () => {

    pageHTML = await axios.get('https://s.cafef.vn/Lich-su-giao-dich-FPT-1.chn');

    const $ = cheerio.load(pageHTML.data);

    data = [];

    // $(".Item_DateItem").each((index, element) => { 
    //     const date = $(element).text(); 
    //     data.push({date: date});
    // });

    // $(".LastItem_Price").each((index, element) => { 
    //     const last_item = $(element).text();
    //     data.push({last_item}); 
    // })

    // $(".Item_Price10").each((index, element) => { 
    //     const item_price = $(element).text();
    //     data.push({item_price}); 
    // })

    $(".cf_ResearchDataHistoryInfo").each((index, el) => {
        date = $(el).find('.Item_DateItem').text();
        last = $(el).find('.LastItem_Price').text();
        data.push({date, last});
    })


    fs.writeFileSync('data.json', JSON.stringify(data));
}

getHTML();