
import os

class Config():

    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    PICDIR = os.path.join(BASEDIR, 'pic')
    
    M_PREFIX = '!'  # 訊息字首
    s1 = '我那時候以為我是被綠💚你才跟我分手的😢😢我沒有要跟你分手的意思😩我那時候想妳前一個禮拜說分手後還會喜歡我😍😍然後這個禮拜馬上又跟另一個男生走那麼近🤬🤬我是人💁會吃醋🤕💔'
    s2 = '對不起 以後我不會再關心你\n我的問題 我的錯\n抱歉 這麼久以來打擾你的生活\n我會消失在你的眼前\n永遠消失'
    s3 = '你不要密我了！🤢🤢我有男盆友了～😤😊🥰🥰掰掰唷 你要加油～😼😼😼考上好大學唷 😻😻😻'
    MESSAGR_DIR = {
        f'{M_PREFIX}排球' : ['接球!','殺球!',"舉球!"],
        f'{M_PREFIX}!抽籤' : ['https://www.youtube.com/watch?v=DLAWa4i_QEI****&feature=youtu.be','小月','訂閱我的youtobe','吉','大吉','小吉','危','大危','超激危!!!','超激不危'],
        f'{M_PREFIX}救救命' : ['🏷抽籤: \n!抽籤','🏐玩排球: \n!排球',"📄逐字稿: \n!逐字稿","🎞照片類: \n!圖片 \n!葉煥軍 \n!胡爾芳 \n!胡爾芳圖片 \n!憨包 \n!yoga "],
        f'{M_PREFIX}逐字稿' : [s1, s2, s3,'有病要看醫生啊','你的感覺我哪次沒考慮過 但你的偏激真的有點噁==','看你是先被鬼上還是先被我上啦 ^^','xji6vm06j06'],
        f'{M_PREFIX}葉煥軍' : ['胡爾芳智障'],
        f'{M_PREFIX}胡爾芳' : ['有笑容的你最好看了🥰'],
        f'{M_PREFIX}557' : ['你們都一樣!!!😭😭'],
        f'{M_PREFIX}小橘子' : ['你很好你真的特別好😩😩'],
    }

    PREFIX_MESSAGE_DIR = {
        f'{M_PREFIX}幫我決定' : ['好啊',"不要"],
        f'{M_PREFIX}我會' : ['會','不會','可能ㄛ'],
    }


