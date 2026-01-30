import azure.functions as func
import requests
import os

app = func.FunctionApp()


@app.function_name(name="CopilotMetricsFetcher")
@app.schedule(schedule="0 */1 * * * *", arg_name="timer", run_on_startup=True)
@app.blob_output(
    arg_name="outputblob",
    path="copilot-metrics/latest-28-days.json",
    connection="AzureWebJobsStorage",
)
def fetch_copilot_metrics(timer: func.TimerRequest, outputblob: func.Out[str]) -> None:
    enterprise = os.environ["GITHUB_ENTERPRISE"]
    token = os.environ["GITHUB_TOKEN"]

    response = requests.get(
        f"https://api.github.com/enterprises/{enterprise}/copilot/metrics",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )

    outputblob.set(response.text)
