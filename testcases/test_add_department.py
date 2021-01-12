import pytest

from page.main_page import MainPage


class TestAddDepartment:
    def setup_class(self):
        self.main=MainPage()

    def teardown_class(self):
        self.main.driver.quit()
    @pytest.mark.parametrize("name,expect",[("质量部05","新建部门成功"),("质量部04","该部门已存在")],ids=['add_sucess','add_fail'])
    def test_add_department(self,name,expect):
        result1=self.main.goto_contact().goto_add_department().add_department(name).get_tips()
        result2=self.main.goto_contact().get_department_list()
        assert result1==expect and name in result2

        # result3 = self.main.goto_contact().goto_add_department().add_department("质量部02").get_tips()
        # assert  result3=="该部门已存在"