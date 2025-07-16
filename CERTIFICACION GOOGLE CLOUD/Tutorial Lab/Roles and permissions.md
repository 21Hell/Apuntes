## Roles and permissions

In addition to cloud computing services, Google Cloud also contains a collection of permissions and roles that define who has access to what resources. You can use the [Cloud Identity and Access Management (Cloud IAM)](https://cloud.google.com/iam/) service to inspect and modify these roles and permissions.
### View your roles and permissions

1. On the **Navigation menu** (![Navigation menu](https://cdn.qwiklabs.com/tkgw1TDgj4Q%2BYKQUW4jUFd0O5OEKlUMBRYbhlCrF0WY%3D "Navigation menu")), click **IAM & Admin > IAM**. This opens a page that contains a list of users and specifies permissions and roles granted to specific accounts.
    
2. Find the student "@qwiklabs" username you signed in with:
    

![Account list with the your Username highlighted](https://cdn.qwiklabs.com/VpeV7knPXEDf39QBcfOJuAZpDB7zPgjzMSFmmCy2avk%3D "Find username")

The _Principal_ column displays `googlexxxxxx_student@qwiklabs.net` (Your matches the username you signed in with). The _Name_ column displays `student XXXXXXXX`. The _Role_ column displays `Editor`, which is one of three _basic roles_ offered by Google Cloud. Basic roles set project-level permissions and, unless otherwise specified, control access and management to all Google Cloud services.

The following table pulls definitions from the [roles documentation](https://cloud.google.com/iam/docs/understanding-roles/#primitive\_roles), which gives a brief overview of viewer, editor, and owner role permissions:

|Role Name|Permissions|
|---|---|
|roles/viewer|Permissions for read-only actions that do not affect state, such as viewing (but not modifying) existing resources or data.|
|roles/editor|All viewer permissions, plus permissions for actions that modify state, such as changing existing resources.|
|roles/owner|All editor permissions and permissions for the following actions: manage roles and permissions for a project and all resources within the project; set up billing for a project.|

As an editor, you can create, modify, and delete Google Cloud resources. However, you can't add or delete members from Google Cloud projects.