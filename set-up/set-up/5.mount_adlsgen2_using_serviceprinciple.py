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

dbutils.secrets.help()

# COMMAND ----------

client_id = dbutils.secrets.get(scope = 'projectformula1-scope', key= 'projectformula1-clientID')
tenant_id = dbutils.secrets.get(scope = 'projectformula1-scope',key = 'projectformula1-tenantID')
client_secret = dbutils.secrets.get(scope = 'projectformula1-scope', key = 'projectformula1-secretID')

# COMMAND ----------

def mount_adls(storage_name,container_name):
    client_id = dbutils.secrets.get(scope = 'projectformula1-scope', key= 'projectformula1-clientID')
    tenant_id = dbutils.secrets.get(scope = 'projectformula1-scope',key = 'projectformula1-tenantID')
    client_secret = dbutils.secrets.get(scope = 'projectformula1-scope', key = 'projectformula1-secretID')


    configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}
    
    if any(mount.mountPoint == f"/mnt/{storage_name}/{container_name}" for mount in dbutils.fs.mounts()):
        dbutils.fs.unmount(f"/mnt/{storage_name}/{container_name}")

    dbutils.fs.mount(
    source = f"abfss://{container_name}@{storage_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_name}/{container_name}",
    extra_configs = configs)
    
    display(dbutils.fs.mounts())






# COMMAND ----------

mount_adls('projectformula1','demo')

# COMMAND ----------

# MAGIC %md
# MAGIC ####Mount raw container

# COMMAND ----------

mount_adls('projectformula1','raw')

# COMMAND ----------

# MAGIC %md
# MAGIC ####mount processed container
# MAGIC

# COMMAND ----------

mount_adls('projectformula1','processed')

# COMMAND ----------

# MAGIC %md
# MAGIC ####mount presentation container
# MAGIC

# COMMAND ----------

mount_adls('projectformula1','presentation')

# COMMAND ----------

