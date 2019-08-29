
class autofocus(object):
    def __init__(self):
        pass

    def run(self):
        print("auto focus run")


'''
1. 검출 시작 클릭 -> button(로컬업로드, URL 업로드, 영상 내려받기, 미디어 control, 검출시작, 검출 대상 리스트(추출 도중 변경 가능시에는 제외)) 사용 불가 
    -> 탭 이동시 경고창 팝업(현재 진행중인 검출 결과가 사라집니다. 중지하겠습니까? Y/N)
    -> before 첫 프레임 부터 play -> after는 포커싱 되는 즉시 결과를 play
    -> 포커싱 완료 후 비활성화된 button(처음 시작시 비활성화된 버튼, after player 미디어 ocntrol 버튼)을 다시 활성화, '포커싱이 완료되었습니다' 팝업 

2. 검출시작 -> 이전 결과 확인 -> 결과가 있으면 이전 결과를 불러오겠습니까? Y/N 팝업창 -> N일 때 1번 과정과 동일
            -> Y일 때 이전 결과 불러오기


2. 공통 변수
    - self.width : 설정의 넓이값
    - self.height : 설정의 높이값
    - self.selected_class : 선택된 클래스
    - self.uploadPath : common의 uploadpath오 동일
    - self.predict : coommon class or facenet_model class

3. 기능
    - 오토 포커싱 영역 조회 : ?????

    - 오토포커싱 영역 중심접 좌표 검출 
       result : x,y,width, height 좌표를 리턴한다.
       ㄴ 학습된 모델에서 frame에서 예측된 결과를 받는다.
       ㄴ 예측된 결과와 설정된 width, height를 바탕으로 오토포커싱 결과를 리턴한다.

    - 오토포커싱 영상 추출 : 
        ㄴ 영상 추출 도중 영상 재생을 위해서 signal을 이용하여 QImage, QRect(추출 결과를 형식 변환) emit
        ㄴ 검출 도중 play 방안
           방안 1. 검출 중에는 현재 Thread에서 before, after player를 모두 play(이와 같이하면 정상속도로 play 되지는 않더라도 동시에 play 가능
           방안 2. before 영상은 common의 plauer thread에서 재생, auto focusing 영상은 현 autofuocus class에서 재생. 
                이 때 영상간의 속도 차이를 줄일 수 있는 방안을 따로 생각해야 함

    - 결과 영상 재생 : 오토포커싱 완료 후 결과를 재생한다. signal을 활용하여  

    - 미디어 플레이어 간 버튼 액션 공유
       ㄴ 공유하기 전에 영상에 대한 오토 포커싱이 완료되어야 한다.
       ㄴ 공유하기 위해서는 같은 slot에 connect


    - 오토 포커싱 결과 저장
        afc_result_save(video_name, result)
        result : frame_num, x_pos, y_pos, width, height

    - 오토 포커싱 결과 조회 : 추출 시작 전 이전 추출 결과가 있는지 확인 있을 시 팝업창을 띄워 이전 결과를 불러올 

    - 오토포커싱 추출 클래스 변경 : 재생중 가능할 때 구현( 필요한 기능 구현 완료 후 구현)
'''