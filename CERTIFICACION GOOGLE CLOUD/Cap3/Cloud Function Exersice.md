
## Task 1. Create a function

First, you're going to create a simple function named helloWorld. This function writes a message to the Cloud Functions logs. It is triggered by cloud function events and accepts a callback function used to signal completion of the function.

For this lab the cloud function event is a cloud pub/sub topic event. A pub/sub is a messaging service where the senders of messages are decoupled from the receivers of messages. When a message is sent or posted, a subscription is required for a receiver to be alerted and receive the message. To learn more about pub/subs, in Cloud Pub/Sub Guides, see [Google Cloud Pub/Sub: A Google-Scale Messaging Service](https://cloud.google.com/pubsub/architecture).

To learn more about the event parameter and the callback parameter, in Cloud Functions Documentation, see [Background Functions](https://cloud.google.com/functions/docs/writing/background).

To create a cloud function:

1. In Cloud Shell, run the following command to set the default region:

```
gcloud config set compute/region REGION
```
2. Create a directory for the function code:
```
mkdir gcf_hello_world
```
3. Move to the `gcf_hello_world` directory:
```
cd gcf_hello_world
```
```
nano index.js
```

```js
/**
* Background Cloud Function to be triggered by Pub/Sub.
* This function is exported by index.js, and executed when
* the trigger topic receives a message.
*
* @param {object} data The event payload.
* @param {object} context The event metadata.
*/
exports.helloWorld = (data, context) => {
const pubSubMessage = data;
const name = pubSubMessage.data
    ? Buffer.from(pubSubMessage.data, 'base64').toString() : "Hello World";

console.log(`My Cloud Function: ${name}`);
};
```
## Task 2. Create a cloud storage bucket

```
gsutil mb -p [PROJECT_ID] gs://[BUCKET_NAME]
```

- **PROJECT_ID** is the Project ID in the lab details panel on the left of this lab:
`qwiklabs-gcp-01-fda3d7faa2f6`

- **BUCKET_NAME** is the name you give to the bucket. You can use the Project ID as the bucket name to ensure a globally unique name:

`qwiklabs-gcp-01-fda3d7faa2f6`
```
gsutil mb -p qwiklabs-gcp-01-fda3d7faa2f6 gs://qwiklabs-gcp-01-fda3d7faa2f6
```
## Task 3. Deploy your function

When deploying a new function, you must specify `--trigger-topic`, `--trigger-bucket`, or `--trigger-http`. When deploying an update to an existing function, the function keeps the existing trigger unless otherwise specified.

For this lab, you'll set the `--trigger-topic` as `hello_world`.

1. Deploy the function to a pub/sub topic named **hello_world**, replacing `[BUCKET_NAME]` with the name of your bucket:
```
gcloud functions deploy helloWorld \
  --stage-bucket [BUCKET_NAME] \
  --trigger-topic hello_world \
  --runtime nodejs20
```

**Note:** If you get OperationError, ignore the warning and re-run the command.

If prompted, enter `Y` to allow unauthenticated invocations of a new function.

2. Verify the status of the function:

```
gcloud functions describe helloWorld
```

## Task 4. Test the function

```
DATA=$(printf 'Hello World!'|base64) && gcloud functions call helloWorld --data '{"data":"'$DATA'"}'
```

