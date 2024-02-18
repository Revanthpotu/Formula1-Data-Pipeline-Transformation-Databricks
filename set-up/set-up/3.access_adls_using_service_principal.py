# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ####Create a Service Principal:
# MAGIC In Azure, you can create a service principal either through the Azure portal, Azure CLI, or Azure PowerShell. This involves creating an application registration, which generates a client ID and client secret (or certificate), and associating it with a role or roles that grant access to the data lake

# COMMAND ----------

# MAGIC %md
# MAGIC ### Access Azure Data Lake using Service Principal
# MAGIC #### Steps to follow
# MAGIC 1. Register Azure AD Application / Service Principal
# MAGIC 2. Generate a secret/ password for the Application
# MAGIC 3. Set Spark Config with App/ Client Id, Directory/ Tenant Id & Secret
# MAGIC 4. Assign Role 'Storage Blob Data Contributor' to the Data Lake. 

# COMMAND ----------

client_id = "217d54a8-8e5b-482a-8612-a08995f257df"
tenant_id = "a7f32339-31ef-4fcd-ad03-58a33afc1431"
client_secret = "fwf8Q~1SPpz-uzNk5EVB5ufGtdnVpLm2Tgkx3dBm"

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.projectformula1.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.projectformula1.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.projectformula1.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.projectformula1.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.projectformula1.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@projectformula1.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@projectformula1.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------

