#coding:utf-8
from Common import baseOperator as BO
import logging
import json
import datetime

#新增商品
goodsdata={
    'addgoogstype':[0,1,2],
    'logisticsType.for':0,
    'goodsName.for':u"非手动新增实物商品"+str(datetime.date.today().strftime("%Y.%m.%d %H%M")),
    'goodsSubTitle.for':u"副标题副标题副标题",
    'goodsClassifyId.selected':'',#商品分类 调用三级联动窗口？
    'goodsBrandId.selected':'',#商品品牌 调用三级联动窗口？
    'goodsMinQuantity.for':2,#最小起订量
    'goodsGroups.selected':'',#商品分组 调用三级联动窗口？
    #'goodsPerMaxNum.for':[2,4],#每2天最多购买4
    'goodsBarCode.for':'',#商品条形码
    'goodsKeyWord.for':'',#关键词
    'maxBuyNum.for':3,#订单限购
    'graySpan.class':'',#商品保障，class
    'skuFlag.class':'',#单一规格，多规格 class
    'tabPane.class':[{
        'inventory':100,#库存
        'kg':1,#重量
        'price':9.1,#拍获价
        'marketprice':100,#市场价
        'supplyprice':88.88,#供货价
        'goosdscode':''#商品编码
    }],#规格表class
    'mainImg.class':[u'./config/商品主图.jpg',u'./config/商品主图.jpg'],#商品主图class
    'videoContainer.id':u'./config/商品视频.mp4',#商品视频id
    'editor-container.iframe.ueditor_0':'',#图文详情id div#id iframe#ueditor_0
    'setupmethod.none':'',#通过查找：设置上架 wording找其父亲div的兄弟，可不用
    'commit.class':'',#class poi3>button
    'goodsPostageId.for':'',#运费模板id,只有实物商品存在
    'addressName.class':'',#不配送区域，方式如何？

}

def bloggin(driver,name,password):
    try:
        driver.ECsends("input", name, 0)
        driver.ECsends("input", password, 1)
        driver.ECclick("button")
        assert("成功"in driver.findElementByClassName("div.el-message").findElementByTagName('p').text)
        logging.log(logging.INFO, "登录成功")
    except Exception:
        #logging.log(logging.ERROR,"登录失败")
        logging.info("登录失败，密码或用户名错误")

if __name__=="__main__":
    keys = goodsdata.keys()
    for i in range(0, len(keys)):
        names = keys[i].split('.')
        print len(names)
        print type(names[0])
        print names[1]
