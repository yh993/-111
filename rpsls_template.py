#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��ֻ�
���ڣ�2021/5/30
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(player_choice):
    """
    ����Ϸ�����Ӧ����ͬ������
    """ 
    if player_choice== "ʯͷ":
	       return 0
    elif player_choice=="ʷ����":
	       return 1
    elif player_choice== "ֽ":
	       return 2
    elif player_choice == "����":
	       return 3
    else:
	       return 4
 # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������  # ��Ҫ���Ƿ��ؽ��
   

 #��дִ�д���,������ɺ�passɾ��


def number_to_name(comp_number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if comp_number == 0:
	       return'ʯͷ'
    elif comp_number ==1:
	       return 'ʷ����'
    elif comp_number == 2:
	       return 'ֽ'
    elif comp_number == 3:
	       return '����'
    else:
	       return '����'
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

 #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ�� print("�����Ӯ��")
    """
    player_number=name_to_number(player_choice)
    print("����ѡ��Ϊ:",player_choice)
    comp_number=random.randrange(0,4)
    comp_choice=number_to_name(comp_number)
    print("�������ѡ��Ϊ:",comp_choice)
    if player_number == comp_number:
		             print("���ͼ��������һ����")
    elif (player_number == 0 and comp_number == 3)or(player_number == 0 and comp_number== 4):
	                 print("��Ӯ��")
    elif (player_number == 1 and comp_number == 0)or(player_number == 1 and comp_number == 4):
	                 print("��Ӯ��")
    elif (player_number== 2 and comp_number == 0)or(player_number == 2 and comp_number == 1):
	                 print("��Ӯ��")
    elif (player_number == 3 and comp_number == 1)or(player_number == 3 and comp_number == 2):
	                 print("��Ӯ��")  
    elif (player_number== 4 and comp_number== 2)or(player_number == 4 and comp_number ==3):
	                 print("��Ӯ��")
    else:
	                 print("�����Ӯ��")  
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

   #����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("---------------------")
print("����������ѡ��:")
player_choice=input()
rpsls(player_choice)
