from Searchsql import GetVerifyCode as gt

g=gt.GetVerifyCode()
cur=g.connect_sql('m2c_users')
print g.excute_sql(cur,"select verify_code from t_support_verify_code WHERE created_date=(select MAX(created_date) FROM  t_support_verify_code WHERE mobile='13500000046')")
