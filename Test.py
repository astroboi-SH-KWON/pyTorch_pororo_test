from pororo import Pororo

print(Pororo.available_tasks())  # available task list

# # OCR : Optical Character Recognition
# ocr = Pororo(task='ocr')
# ocr_res = ocr("./input/line-indent.png")
# ocr_res = ocr("./input/img_Korean.png")
# print(ocr_res)

from pororo.pororo import SUPPORTED_TASKS
# print(SUPPORTED_TASKS['ocr'].get_available_langs())

# ocr_web = ocr('http://bit.ly/london-sign', detail=True)
# ocr_web = ocr('https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20180525_185%2Fsales1%40printsq.com_1527224954086BfPcc_JPEG%2F50532113707823649_578256427.jpg&type=sc960_832', detail=True)
# print(ocr_web)


# # image captioning
# print(SUPPORTED_TASKS['caption'].get_available_langs())
# caption = Pororo(task='caption', lang='en')
# # cap_exp = caption('http://bit.ly/ny-timesquare')
# cap_exp = caption('https://newsimg.hankookilbo.com/cms/articlerelease/2020/11/28/03584158-b740-4f26-a897-48a7d850d4b7.jpg')
# print(cap_exp)


# # # translation  6 layered encoder, 6 layered decoder
ori_text = '2020년 3월 20일 인도 잠무에서 코로나19 확산을 막기 위해 전국이동제한령 및 식품, 의약품 등 필수 목적을 제외한 상점이 폐쇄된 가운데 잠무시 보건요원이 인적이 드문 시장에서 방역작업을 하고 있다. '

# mt = Pororo(task='translation', lang='multi')
# trn_text = mt(ori_text, src='ko', tgt='en')
# print(trn_text)

# # # translation  12 layered encoder, 1 layered decoder
# faster_mt = Pororo(task='translation', lang='multi', model='transformer.large.multi.fast.mtpg')
# fast_trn_txt = faster_mt(ori_text, src='ko', tgt='en')
# print(fast_trn_txt)



# # # text summarization
# ori_text = """
# 국내 신종 코로나바이러스 감염증(코로나19) 백신 접종 사전예약시스템에서 시간당 200만명까지 예약이 가능해진다. 본인이 아닌 대리예약이나 동시접속은 허용되지 않는다.
# 코로나19 예방접종대응추진단(이하 추진단)은 5일 과학기술정보통신부·행정안전부와 부처 합동 브리핑에서 '먹통 사태' 등 오류 해결을 위해 민·관 협력으로 이같이 사전예약시스템을 개선했다고 밝혔다.
# 추진단은 서버 확충과 재배치, 데이터베이스(DB) 효율화 등을 통해 원활한 접속이 가능해져 시간당 30만건에서 200만건까지 예약처리 성능이 향상될 것으로 예상한다.
# 추진단에 따르면 오는 9일 '10부제 예약' 형태로 시작되는 18~49세 일반 청장년층 사전예약 시 최대 인원이 동시에 접속해도 30~50분이면 예약이 끝난다.
# 주민등록번호 생년월일 끝자리를 기준으로 예약일자를 열흘에 걸쳐 나누는 '10부제 예약'이 도입되면 예약 대상자는 이날 0시 기준 1천621만명 가운데 하루 최대 190만명(11.7%) 수준으로 유지돼 분산 효과가 생긴다.
#
# 10부제 예약 기반에서 '본인인증수단 다양화', '대리예약·동시접속 제한' 등도 도입돼 종전보다 원활한 접속이 가능하다.
# 본인인증은 휴대전화, 아이핀, 공동·금융인증서 등이 아닌 간편인증서를 통해 빠르게 할 수 있다. 카카오, 네이버, 패스(PASS) 애플리케이션 등에서 인증서를 미리 발급받으면 예약이 쉬워진다. 종전과 달리 본인인증을 먼저 하고 예약 대기를 거쳐야 한다.
# 김은주 한국지능정보사회진흥원 단장은 "간편인증을 이용할 때 적어도 하루 전에 인증서를 사전에 발급받아야 예약 당일 별도의 지체 없이 인증을 진행할 수 있다"고 안내했다.
# 특히 본인인증 수단별 실시간 상태 정보를 녹색(원활), 황색(지연), 적색(혼잡), 회색(선택 불가) 등 신호등 방식으로 한눈에 볼 수 있어 예약자가 사전에 확인 후 혼잡이 없는 방식을 선택할 수 있다.
# 예약은 당일 오후 8시부터 다음 날 오후 6시까지 가능하다. 김 단장은 "예약이 집중될 것으로 예상되는 오후 8시를 피해 오후 9시 이후부터 이용하면 빠르게 예약할 수 있다"고 설명했다.
# 접속 대기를 할 땐 앞에 여러 명이 대기할 경우 재접속하지 않고 좀 더 기다리는 게 낫다. 재접속할 경우 예약시간이 더 길어질 수 있다.
# 또 과도한 대기를 막기 위해 대리예약은 허용되지 않으며, 한 사람이 여러 단말기로 동시에 사전예약을 시도할 경우 최초 본인인증이 완료된 단말기 이외에는 10분간 본인인증이 차단된다.
# """

# abs_smm = Pororo(task='summary', lang='ko', model='abstractive')
# smm_res = abs_smm(ori_text)
# print(smm_res)

# bul_summ = Pororo(task='summary', lang='ko', model='bullet')
# bul_res = bul_summ(ori_text)
# print(bul_res)

# ext_summ = Pororo(task='summary', lang='ko', model='extractive')
# ext_res = ext_summ(ori_text)
# print(ext_res)



# # sentiment analysis
# sa_shop = Pororo(task="sentiment", model="brainbert.base.ko.shopping", lang="ko")
# sa_shop = Pororo(task="sentiment", model="brainbert.base.ko.nsmc", lang="ko")
# sa_res = sa_shop('정말 혼자 공부하기 너무 좋은 머신러닝 독학 책')
# print(sa_res)


# # natural language inference
# nli = Pororo(task='nli', lang='ko')
# nli_res = nli("저는, 그냥 알아내려고 거기 있었어요", "나는 처음부터 그것을 잘 이해했다")
# print(nli_res)



# # zero-shot topic classification
# zsl = Pororo(task='zero-topic', lang='ko')
# zsl_res = zsl('손흥민이 골을 넣었다', ['정치', '사회', '스포츠', '연예'])
# print(zsl_res)


mrc = Pororo(task="mrc", lang="ko")
mrc_res = mrc("카카오브레인이 공개한 라이브러리 이름은?", "카카오브레인은 자연어 처리와 음성 관련 태스크를 쉽게 수행할 수 있도록 도와 주는 라이브러리 pororo를 공개하였습니다.", postprocess=False)
print(mrc_res)
# pip install python-mecab-ko