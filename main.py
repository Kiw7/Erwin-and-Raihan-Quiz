import mid
import os

if __name__ == "__main__":
    quiz = mid.StudiKasus2('localhost', '3306', 'root', os.environ["MYSQL_PASSWORD"])
    df = quiz.import_csv('annualenterprise.csv')
    print(quiz.create_db('business'))
    print(quiz.create_table('business', 'users', df))
    print(quiz.load_data('business', 'users'))