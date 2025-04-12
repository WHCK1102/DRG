# DRG: A Dual Relational Graph Framework for Course Recommendation
## Dataset

The dataset used is from the MOOC series dataset. The task is to generate the course question that the user is most likely to interact with based on the input. See the "data" folder of this project, where each sample is a line in the following format:
```json
{
        "input": "用户A曾经交互过操作系统，大数据系统基础等课程，请你从剩下的电工技术，PLC应用技术，程序设计基础，汇编语言程序设计，微机原理与接口技术，20世纪西方音乐，Web开发技术，公共危机管理，流计算、内存计算与分布式机器学习平台（微慕课），化工单元过程与操作，应对气候变化的中国视角，思想道德修养和法律基础，国际金融，现代管理学，无处不在传染病，生活英语听说，自动控制元件，概率论与数理统计，微积分B(2)，2017年清华大学研究生学位论文答辩（一），计算思维导论，美国政治概论等课程中选出用户A最有可能交互的一些课程，最多20个",
        "output": "程序设计基础，汇编语言程序设计"
},
```
## Image

The specific process is as follows:
![MACRO](https://github.com/WHCK1102/MACRO/blob/main/images/figure2.jpg)
## Prompt
### LLM-based Course Attributes Augmentation

Prompt1

You are a senior university course planner, skilled in recommending the next course of interest to students based on their course history and learning sequence. Given the user's interacted course \{History Course\}, select the most likely course $c^{+}$ from the remaining \{Candidate Courses 1\}. The output format should be \{History Course, $c^{+}$\}.

Prompt2

You are a senior university course planner,  Based on the user's historical interaction records \{History Course\}, analyze and predict the next courses they might be interested in $c^{+}$, selecting from courses in the same category \{Candidate Courses2\}  those previously interacted with. The output in the format \{History Course, $c^{+}$\}.

### LLM-based User Profile Augmentation

Prompt1

You are a senior university course planner, please predict the course \{$c^{+}$\} that the user may be interested in next, based on the user's historical interaction records \{History Course\}, and the candidate courses \{Candidate Courses 3\} that neighboring users have interacted with. The output format should be \{History Course, $c^{+}$\}.

Prompt2

You are a senior university course planner, please predict the course \{$c^{+}$\} that the user may be interested in next, based on the user's historical interaction records \{History Course\},and the candidate courses \{Candidate Courses 4\} that similar users have interacted with. The output format should be \{History Course, $c^{+}$\}.
