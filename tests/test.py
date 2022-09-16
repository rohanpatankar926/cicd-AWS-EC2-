import requests

class Test:
  def test_index():
      response = requests.get("http://127.0.0.1:8000/")
      assert response.status_code == 200
 
 if __name__=="__main__":
      Test.test_index()
