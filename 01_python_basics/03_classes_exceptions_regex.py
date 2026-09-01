"""Python 기초: 클래스, 예외처리, 정규표현식

데이터 분석에서 자주 사용되는 고급 기초 문법입니다.
클래스를 통한 객체 지향 프로그래밍, 에러 처리, 텍스트 패턴 매칭을 배웁니다.
"""

import re
from datetime import datetime


# ============================================================================
# 1. 클래스 (Class) - 객체 지향 프로그래밍
# ============================================================================

class Student:
    """학생 정보를 관리하는 클래스"""
    
    # 클래스 변수 (모든 인스턴스가 공유)
    total_students = 0
    
    def __init__(self, name, student_id, scores):
        """
        생성자: 객체 생성시 자동으로 실행됨
        
        Parameters:
            name (str): 학생 이름
            student_id (str): 학번
            scores (list): 점수 리스트
        """
        self.name = name
        self.student_id = student_id
        self.scores = scores
        Student.total_students += 1
    
    def get_average(self):
        """평균 점수 계산"""
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
    
    def get_grade(self):
        """학점 판정"""
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    def __str__(self):
        """객체를 문자열로 표현"""
        return f"{self.name} (학번: {self.student_id}): 평균 {self.get_average():.2f}점, 학점: {self.get_grade()}"
    
    def __repr__(self):
        """객체의 공식 문자열 표현"""
        return f"Student(name='{self.name}', id='{self.student_id}', avg={self.get_average():.2f})"


# 클래스 사용 예제
print("=" * 70)
print("1. 클래스 (Class) - 객체 지향 프로그래밍")
print("=" * 70)

student1 = Student("김민수", "2024001", [90, 85, 88, 92])
student2 = Student("이영희", "2024002", [78, 82, 80, 85])
student3 = Student("박준호", "2024003", [95, 93, 97, 94])

print(student1)
print(student2)
print(student3)
print(f"\n총 학생 수: {Student.total_students}명\n")


# 상속 (Inheritance) 예제
class AdvancedStudent(Student):
    """고급 기능이 추가된 학생 클래스"""
    
    def __init__(self, name, student_id, scores, major):
        super().__init__(name, student_id, scores)  # 부모 클래스 생성자 호출
        self.major = major
    
    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} | 전공: {self.major}"


advanced_student = AdvancedStudent("최정민", "2024004", [92, 94, 91, 95], "데이터과학")
print(f"상속 예제: {advanced_student}\n")


# ============================================================================
# 2. 예외처리 (Exception Handling)
# ============================================================================

print("=" * 70)
print("2. 예외처리 (Exception Handling)")
print("=" * 70)

def safe_average(scores):
    """
    안전하게 평균을 계산하는 함수
    예외가 발생하면 적절히 처리합니다.
    """
    try:
        if not isinstance(scores, list):
            raise TypeError("scores는 리스트여야 합니다")
        
        if len(scores) == 0:
            raise ValueError("최소 1개 이상의 점수가 필요합니다")
        
        # 모든 요소가 숫자인지 확인
        if not all(isinstance(score, (int, float)) for score in scores):
            raise TypeError("모든 점수는 숫자여야 합니다")
        
        avg = sum(scores) / len(scores)
        return avg
    
    except TypeError as e:
        print(f"타입 에러: {e}")
        return None
    
    except ValueError as e:
        print(f"값 에러: {e}")
        return None
    
    except Exception as e:
        print(f"예상하지 못한 에러: {e}")
        return None
    
    finally:
        print("  → 평균 계산 함수 실행 완료\n")


# 정상 사용
print("정상 사용:")
result = safe_average([90, 85, 88, 92])
print(f"결과: {result}\n")

# 에러 케이스 1: 빈 리스트
print("에러 케이스 1 - 빈 리스트:")
result = safe_average([])

# 에러 케이스 2: 잘못된 타입
print("에러 케이스 2 - 잘못된 타입:")
result = safe_average([90, "85", 88])

# 에러 케이스 3: 리스트가 아닌 값
print("에러 케이스 3 - 리스트가 아닌 값:")
result = safe_average("90, 85, 88")


# with 문을 이용한 파일 처리 (안전한 리소스 관리)
print("=" * 70)
print("파일 처리시 예외 처리 예제:")
print("=" * 70)

try:
    # 임시 파일 생성 및 읽기
    with open("/tmp/temp_data.txt", "w", encoding="utf-8") as f:
        f.write("점수: 90, 85, 88, 92\n")
        f.write("이름: 민수, 영희, 준호\n")
    
    # 파일 읽기
    with open("/tmp/temp_data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print("파일 내용:")
        for line in lines:
            print(f"  {line.strip()}")
    
    print("파일 처리 성공!\n")

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

except IOError as e:
    print(f"파일 입출력 에러: {e}")


# ============================================================================
# 3. 정규표현식 (Regular Expression)
# ============================================================================

print("=" * 70)
print("3. 정규표현식 (Regular Expression)")
print("=" * 70)

# 3.1 기본 패턴 매칭
print("\n3.1 기본 패턴 매칭:")
print("-" * 70)

text = "한국 대학교의 학생들: 학번 2024001, 2024002, 2024003"
pattern = r"\d{4}\d{3}"  # 숫자 7개

matches = re.findall(pattern, text)
print(f"텍스트: {text}")
print(f"패턴 (\\d{{4}}\\d{{3}}): {matches}")

# 3.2 이메일 주소 검증
print("\n3.2 이메일 주소 검증:")
print("-" * 70)

email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

emails = [
    "user@example.com",
    "invalid.email@",
    "test123@domain.co.kr",
    "no-at-sign.com",
    "hello@world.org"
]

for email in emails:
    is_valid = bool(re.match(email_pattern, email))
    status = "✓ 유효" if is_valid else "✗ 무효"
    print(f"{email:25} {status}")

# 3.3 전화번호 추출
print("\n3.3 전화번호 추출:")
print("-" * 70)

text = "연락처: 010-1234-5678, 02-123-4567, 031-1234-5678"
phone_pattern = r"\d{2,3}-\d{3,4}-\d{4}"

phones = re.findall(phone_pattern, text)
print(f"텍스트: {text}")
print(f"추출된 전화번호: {phones}\n")

# 3.4 문자열 치환
print("3.4 문자열 치환:")
print("-" * 70)

text = "I am learning Python, Python is great. python is fun!"
new_text = re.sub(r"[Pp]ython", "PYTHON", text)
print(f"원본: {text}")
print(f"변환: {new_text}\n")

# 3.5 날짜 형식 추출
print("3.5 날짜 형식 추출:")
print("-" * 70)

text = "날짜: 2024-09-01, 2024/09/02, 09-03-2024"
date_pattern = r"\d{4}[-/]\d{2}[-/]\d{2}"

dates = re.findall(date_pattern, text)
print(f"텍스트: {text}")
print(f"추출된 날짜: {dates}\n")

# 3.6 그룹 추출 (Grouping)
print("3.6 그룹 추출 (Grouping):")
print("-" * 70)

text = "John: john@example.com, Jane: jane@example.com"
pattern = r"(\w+):\s*(\S+@\S+)"

matches = re.findall(pattern, text)
print(f"텍스트: {text}")
print("추출된 그룹:")
for name, email in matches:
    print(f"  이름: {name}, 이메일: {email}\n")


# ============================================================================
# 4. 통합 예제: 학생 데이터 처리
# ============================================================================

print("=" * 70)
print("4. 통합 예제: 학생 데이터 처리")
print("=" * 70)

class StudentDataProcessor:
    """학생 데이터를 처리하는 클래스 (클래스 + 예외처리 + 정규표현식)"""
    
    def __init__(self, data_string):
        """
        데이터 문자열에서 학생 정보를 추출하여 초기화
        
        데이터 형식:
        "이름(학번): 점수1,점수2,점수3 | 이메일"
        예: "민수(2024001): 90,85,88 | kim@example.com"
        """
        self.data_string = data_string
        self.students = []
        self._parse_data()
    
    def _parse_data(self):
        """데이터 문자열 파싱"""
        try:
            # 학생 정보 분리 (;로 구분)
            student_records = self.data_string.split(";")
            
            for record in student_records:
                record = record.strip()
                if not record:
                    continue
                
                # 정규표현식으로 데이터 추출
                pattern = r"(\w+)\((\d+)\):\s*([\d,]+)\s*\|\s*(\S+@\S+)"
                match = re.match(pattern, record)
                
                if not match:
                    raise ValueError(f"잘못된 형식: {record}")
                
                name, student_id, scores_str, email = match.groups()
                scores = [int(s.strip()) for s in scores_str.split(",")]
                
                student = {
                    "name": name,
                    "student_id": student_id,
                    "scores": scores,
                    "email": email
                }
                
                self.students.append(student)
        
        except ValueError as e:
            print(f"파싱 에러: {e}")
        except Exception as e:
            print(f"예상하지 못한 에러: {e}")
    
    def display_summary(self):
        """학생 정보 요약 출력"""
        print(f"\n총 {len(self.students)}명의 학생 정보:\n")
        for student in self.students:
            avg = sum(student["scores"]) / len(student["scores"])
            print(f"  • {student['name']} ({student['student_id']})")
            print(f"    점수: {student['scores']}, 평균: {avg:.2f}")
            print(f"    이메일: {student['email']}\n")


# 통합 예제 실행
data = """
민수(2024001): 90,85,88,92 | kim@example.com;
영희(2024002): 78,82,80,85 | lee@example.com;
준호(2024003): 95,93,97,94 | park@example.com
"""

processor = StudentDataProcessor(data)
processor.display_summary()

print("=" * 70)
print("학습 완료!")
print("=" * 70)
