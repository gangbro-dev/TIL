# HTML

## 목차

## HTML 개요
  - Hyper Text Markup Language의 약자이다.
    - 하이퍼텍스트란, 참조(하이퍼링크)를 통해서 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
  - HTML은 웹의 구조, 뼈대를 짜는 언어이다.
  - HTML은 웹페이지의 표시를 위해서 만들어진 마크업 언어이다.
    - 마크업 언어란, 태그, 기호 등을 이용해서 문서나 데이터의 구조를 명시하는 언어(HTML, MD 등)
  - HTML은 태그라는 요소로 이루어진 구조를 정하는 언어이다.

### 파편화와 웹 표준
  - 웹 사이트는 브라우저를 통해서 동작한다.
  - 하지만, 브라우저마다 동작이 약간씩 달라서 문제가 발생했다.(파편화)
  - 해결책으로 나타난 웹 표준이 존재한다.(W3C, WHATWG 등의 단체)
  - 어떤 브라우저를 사용하더라도 같은 화면을 보여주도록 하는 `크로스 브라우징`을 실현

### HTML의 스타일 가이드
  - 외부 요소와 내부 요소간에 들여쓰기를 통해서 단계를 구분하면, 가독성이 올라간다(권장)

## HTML의 구조

1. HTML : 문서의 최상위 요소
2. head : 문서의 메타데이터
    - 문서 제목, 인코딩, 스타일, 외부파일 로딩 등
    - 일반적으로 브라우저에 나타나지 않음
3. body :  문서 본문 내용
    - 실제 화면구성과 관련된 내용들

--- 

### head

- tltle, meta, link 등 구현과 해석에 필요한 정보들을 넣어두는 구조이다.
- 실제 사이트를 구현할 때는 드러나지 않지만, OGP(Open Graph Protocol) 등 외부링크에 사용되거나, 문서에 머릿말, 꼬릿말 등과 같은 역할을 한다.

### body

- 사용자가 보게 되는 영역
- 웹페이지에서 드러나는 정보는 모두 이곳에서 정의되어 나타난다.
- 3개로 더 세분화해서 `header`, `section`, `footer` 로 나누어 샤용할 수도 있다 (권장)

---

### 요소와 속성
요소


- 요소는 태그와 컨텐츠로 이루어진 HTML을 이루는 구조이다.
- 요소는 시작태그와 종료태그, 그리고 태그 사이에 위치한 내용으로 구성
- 내용이 없는 태그들도 있다.
  - br, hr, img, input, link, meta 와 같이 특수한 기능을 수행하는 태그들
- 요소는 중첩이 가능하다.
  - 요소 내부에서 다시 요소를 시작해서 중첩할 수 있다.
  - 크롬의 개발자 도구를 이용해서 어떤 요소가 화면을 구성하고 잇는지 확인할 수 있다.

속성

- 속성은 요소의 컨텐츠에서 디테일한 값을 지정할 때 사용하는 것이다.
- 속성을 이용해서 구체적인 기능을 구현할 수 있다.
- 보통 이름과 값이 쌍으로 존재한다.
- 태그와 상관없이 사용 가능한 속성도 존재한다.
  ```
  - id : 문서 전체에서 유일한 고유 식별자 지정
  - class : 공백으로 구분도니 해당 요소의 클래스 목록(CSS, JS 에서 활용)  
  - data-* : 페이지에서 개인 사용자 정의 데이터를 저장하기 위해서 사용
  - style : inline 스타일
  - title : 요소에 대한 추가정보
  - tabindex : 요소의 탭 순서
  등등
  ```

시맨틱 태그
- HTML 태그가 특정 목적, 역할 및 의미적 가치(semantic value)를 가지는 것
  - 예를 들어 h1 태그는 "이 페이지의 최상위 제목"인 텍스트를 의미하는 것이다.
  - HTML5 부터 의미론적 요소를 담은 시맨틱 태그를 권장한다.
  - 이러한 표기를 이용해서 태그가 담고있는 목적, 내용 등을 알 수 있다.
- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미있는 정보의 그룹을 태그로 표현
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
- 검색 엔진 최적화(SFO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용 해야함.

 ---

### 랜더링

HTML을 웹페이지로 바꾸기 위해선 랜더링이라는 과정이 필요

DOM(Document Object Model) 트리
- 텍스트 파일인 HTML문서를 브라우저에서 렌더링하기 위한 구조
- HTML 문서에 대한 모델을 의미한다. 문서 내 각 요소에 접군 / 수정에 필요한 것들을 제공

## HTML 문서 구조화

HTML 요소들은 크게 인라인/블록 요소로 나눈다.
- 인라인은 글자처럼 취급하는 요소이다.
- 블록 요소는 한 줄 모두 사용

CSS에서 이것을 이용한다!
```html
텍스트 요소
<a></a> : href 속성을 활용하여 하이퍼링크 생성
<b></b>, <strong></strong> : 굵은 글씨 요소. 중요한 강조하고자 하는 요소
<i></i>, <em></em> : 기울임 글씨 요소. 중요한 강조하고자 하는 요소
<br> : 텍스트 내에 줄바꿈 요소
<img> : src속성을 활용하여 이미지 표현 
<ul> : 구분선 요소
<span></span> : 의미없는 인라인 컨테이너
```
 ---
 
 ### form

- \<form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
- \<form> 기본속성
  - action : form을 처리할 서버의 URL
  - method : form을 체출할 때 사용할 HTTP 메서드(Get 혹은 Post)
  - enctype : method가 post인 경우 데이터의 유형
    - application/x-www-form-urlencoded:기본값
    - multipart/form-data : 파일 전송 시(input type이 file인 경우)
    등

### input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- \<input> 대표적인 속성
  - name : form control에 적용되는 이름
  - value : form controldp 적용되는 값
  - required, readonly, autofocus, autocommplete, disabled 등

<br>

input label
- `label`을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
  - 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일(터치)환경에서 편하게 사용할 수 있음
  - `label`과 `input` 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 `label`을 읽어 쉽게 내용을 확인 할 수 있도록 함.
- \<input>에 id속성을, \<label>에는 for 속성을 활용하여 상호 연관을 시킴

<br>

input 유형 - __일반__
- 일반적으로 입력을 받기 위하여 제공되며, 타입별로 HTML 기본 검증 혹은 추가 속성을 활용할 수 있음
  - text : 일반 텍스트 입력
  - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
  - email : 이메일 형식이 아닌 경우 form 제출 불가
  - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
  - file : accept 속성을 활용하여 파일 타입 지정 가능

input 유형 - __항목 중 선택__
- 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함
- 동일 항목에 대하여는 name을 지정하고, 선택된 항목에 대한 value를 지정해야 함
  - checkbox : 다중 선택
  - radio : 단일 선택

input 유형 - __기타__
- 다양한 종류의 input을 위한 `picker`를 제공
  - color, date 등
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - hidden : 사용자에게 보이지 않는 input

정리
- \<input> 요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지할 것
- 위키백과 등에서 자세히 정리되어 있으므로 확인하고 자기가 원하는 것을 선택하여 활용