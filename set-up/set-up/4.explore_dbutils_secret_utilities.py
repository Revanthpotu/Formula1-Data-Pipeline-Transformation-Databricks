# Databricks notebook source
dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list(scope='projectformula1-scope')

# COMMAND ----------

dbutils.secrets.get(scope ='projectformula1-scope', key = 'projectformula1-key' )

# COMMAND ----------

