# Azure Device Update autorest configuration for Python

### Settings

```yaml
require:
  - https://github.com/Azure/azure-rest-api-specs/blob/9e30496a8803beb5a84909997e5cd7ea0f242fd8/specification/deviceupdate/data-plane/readme.md
output-folder: ../azure/iot/deviceupdate
namespace: azure.iot.deviceupdate
package-name: azure-iot-deviceupdate
license-header: MICROSOFT_MIT_NO_VERSION
clear-output-folder: true
no-namespace-folders: true
python: true
title: DeviceUpdateClient
version-tolerant: true
package-version: 1.0.0b2
add-credential: true
credential-scopes: https://api.adu.microsoft.com/.default
```
