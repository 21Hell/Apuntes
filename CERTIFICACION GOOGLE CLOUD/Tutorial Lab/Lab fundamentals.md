### Features and components
![[Pasted image 20231010220859.png]]

#### Start Lab (button)
Creates a temporary Google Cloud environment
#### Credit
The price of a lab. 1 Credit is _usually_ equivalent to 1 US dollar.
#### Time
When you click the Start Lab button, the timer will count down until it reaches 00:00:00
### Paying for a lab

With an access code or credits

### Reading and following instructions



### Test your understanding


### Lab details pane

Now that your lab instance is up and running, look at the **Lab details** pane on the left. It contains an **Open Google Console** button, credentials (username and password), and a **Project ID** field.

![Lab details pane](https://cdn.qwiklabs.com/%2FtHp4GI5VSDyTtdqi3qDFtevuY014F88%2BFow%2FadnRgE%3D "Lab details pane")

**Note:** Your credentials will resemble but not match the image; every lab instance generates new temporary credentials.

Now examine each of these components.

#### Open Google console

This button opens the [Cloud console](https://cloud.google.com/cloud-console/): the web console and central development hub for Google Cloud. You will do the majority of your work in Google Cloud from this interface.

#### Project ID

A [Google Cloud project](https://cloud.google.com/docs/overview/#projects) is an organizing entity for your Google Cloud resources. It often contains resources and services; for example, it may hold a pool of virtual machines, a set of databases, and a network that connects them together. Projects also contain settings and permissions, which specify security rules and who has access to what resources.

A _Project ID_ is a unique identifier that is used to link Google Cloud resources and APIs to your specific project. Project IDs are unique across Google Cloud: there can be only one **qwiklabs-gcp-xxx....**, which makes it globally identifiable.

#### Username and Password

These credentials represent an identity in the Cloud Identity and Access Management (Cloud IAM) service. This identity has access permissions (a role or roles) that allow you to work with Google Cloud resources in the project you've been allocated. These credentials are _temporary_ and will only work for the access time of the lab. When the timer reaches 00:00:00, you will no longer have access to your Google Cloud project with those credentials.



### Sign in to Google Cloud

Now that you have a better understanding of the **Lab details** pane, use its contents to sign in to the Cloud console.

1. Click **Open Google console**.

This opens the Google Cloud sign-in page in a new browser tab.

If you've ever signed in to a Google application like Gmail, this page should look familiar.

**_Tip_** Open the tabs in separate windows, side-by-side.

**Note:** If the **Choose an account** page opens, click **Use Another Account**. ![Choose an account window highlighting the Use another account option](https://cdn.qwiklabs.com/eQ6xPnPn13GjiJP3RWlHWwiMjhooHxTNvzfg1AL2WPw%3D)

2. The **Username** from the Lab Details pane automatically fills in. Click **Next**.

_Wait! Make sure to use the googlexxxxxx_student@qwiklabs.net email to sign in, NOT your personal or company email address!_

**Note:** The username that resembles googlexxxxxx_student@qwiklabs.net is a Google account that was created for your use as a student. It has a specific domain name, which is "qwiklabs.net," and has been assigned IAM roles that allow you to access the Google Cloud Project that you have been provisioned.

3. Copy the **Password** from the Lab Connection pane, paste it in the **Password** field, and click **Next**.
4. Click **I understand** to indicate your acknowledgement of Google's terms of service and privacy policy.
5. On the **Welcome** page, check **Terms of Service** to agree to Google Cloud's terms of service, and click **Agree and continue**.

You've successfully accessed the Cloud Console with your student credentials! Your page should now look like this:

![Google Cloud console](https://cdn.qwiklabs.com/vPsOw690IZhUlPPxZk3asDaXQBRVZRiyr%2B6nBXCqEf4%3D "Google Cloud console logged in")
