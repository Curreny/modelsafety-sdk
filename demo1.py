#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ModelSafety SDK 演示脚本 - 题库生成

此脚本提供了如何使用ModelSafety SDK的简单示例，用户可以直接修改参数进行测试。
"""
from modelsafety import ModelSafetyClient
client = ModelSafetyClient()

# 1. 题库生成请求
"""
"single": 单选题
"judge": 判断题
"essay": 简答题
"count": 对应题型的题目数量
"""
question_gen_data = {
    "typesRequest": [
        {
            "type": "single",
            "count": 2
        },
        {
            "type": "judge",
            "count": 2
        },
        {
            "type": "essay",
            "count": 2
        }
    ]
}

# 发送题库生成请求
question_result = client.generate_questions(question_gen_data)
print(question_result)




