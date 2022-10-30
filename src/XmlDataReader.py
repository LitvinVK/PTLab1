# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader

import xml.etree.cElementTree as xml
import random


class XmlDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str):
        tree = xml.ElementTree(file=path)
        root = tree.getroot()
        students = list(root)

        for student in students:
            self.key = student.attrib.get("class")
            student_children = list(student)
            self.students[self.key] = []

            for student_child in student_children:
                self.students[self.key].append((student_child.tag,
                                                int(student_child.text)))

        return self.students
        # print(self.students)

        # for student in students:
        #     self.key = student.attrib.get("class")
        #     student_children = list(student)
        #     is100 = True

        #     for student_child in student_children:
        #         if int(student_child.text) != 100:
        #             is100 = False

        #     if is100:
        #         self.students100.append(student.attrib.get("class"))

        # if len(self.students100) == 0:
        #     print("Ни у одного студента нет 100 баллов по всем дисциплинам")
        # else:
        #     print("У студента", self.students100
        #     [random.randint(0, len(self.students100)-1)],
        #     "100 баллов по всем дисциплинам")
