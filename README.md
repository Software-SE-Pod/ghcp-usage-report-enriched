# GitHub Copilot Metrics Fetcher

Azure Function that fetches enterprise Copilot metrics and stores in blob storage.

## Deploy (Windows PowerShell)

```powershell
# Variables
$rg = "rg-copilot-metrics"
$loc = "canadacentral"
$storage = "stcopilotmetrics$(Get-Random -Max 9999)"
$func = "func-copilot-metrics$(Get-Random -Max 9999)"

# Create resources
az group create -n $rg -l $loc
az storage account create -n $storage -g $rg -l $loc --sku Standard_LRS --allow-shared-key-access true
az functionapp create -n $func -g $rg -s $storage --consumption-plan-location $loc --runtime python --runtime-version 3.11 --functions-version 4 --os-type Linux

# Configure
az functionapp config appsettings set -n $func -g $rg --settings GITHUB_ENTERPRISE=your-enterprise-slug GITHUB_TOKEN=your-token

# Deploy
func azure functionapp publish $func
```

## Deploy (Mac/Linux)

```bash
# Variables
rg="rg-copilot-metrics"
loc="eastus"
storage="stcopilotmetrics$RANDOM"
func="func-copilot-metrics$RANDOM"

# Create resources
az group create -n $rg -l $loc
az storage account create -n $storage -g $rg -l $loc --sku Standard_LRS --allow-shared-key-access true
az functionapp create -n $func -g $rg -s $storage --consumption-plan-location $loc --runtime python --runtime-version 3.11 --functions-version 4 --os-type Linux

# Configure
az functionapp config appsettings set -n $func -g $rg --settings GITHUB_ENTERPRISE=your-enterprise-slug GITHUB_TOKEN=your-token

# Deploy
func azure functionapp publish $func
```

## PowerBI

Connect to: `stcopilotmetrics` → container `copilot-metrics` → file `latest-28-days.json`
