# Cisco Defense Orchestrator MCP

Cisco Defense Orchestrator MCP is a Python-based Model Context Protocol (MCP) server for Cisco Defense Orchestrator (CDO). It provides tools for querying the CDO API to discover, monitor, and manage your CDO environment.

**DISCLAIMER: THIS IS CURRENTLY BUILT FOR USE IN A DEVNET ENVIRONMENT FOR POC. SSL VERIFICATION IS DISABLED. THIS IS NOT RECOMMENDED FOR PRODUCTION USE.**

## Features

- **Inventory Management**: Retrieve and manage devices and managers in the CDO inventory
- **Policy Management**: Access and create access policies and rules for cdFMC
- **Object Management**: Manage network objects (placeholder for additional object-related endpoints)
- **User Management**: Retrieve user information (placeholder for user-related endpoints)
- **Network Automation**: Support for bulk operations and API-driven management
- **Advanced Monitoring**: Access to device and policy analytics (expandable based on full API)

## Installation

0. Clone the repository:

  ```
  git clone https://github.com/JackRiebel/Cisco_Security_Cloud_Control_MCP.git
  cd Cisco_Security_Cloud_Control_MCP
  ```

1. Create a virtual environment and activate it:

  ```
  python -m venv .venv
  source .venv/bin/activate  # On Windows: .venv\Scripts\activate
  ```

2. Install dependencies:

  ```
  pip install -r requirements.txt
  ```

## Configuration

0. Copy the example environment file:

  ```
  cp .env-example .env
  ```

1. Update the `.env` file with your CDO API token and base URL (including region, e.g., `us` for `api.us.security.cisco.com`):

  ```
  CDO_API_BASE_URL=https://api.us.security.cisco.com/firewall/v1
  CDO_API_TOKEN=Your_CDO_API_Token_here
  ```

## Usage with Claude Desktop Client

0. Configure Claude Desktop to use this MCP server:

   * Open Claude Desktop
   * Navigate to Settings > Developer > Edit Config
   * Add the following configuration to `claude_desktop_config.json`:

     ```json
     {
       "mcpServers": {
         "CDO_MCP": {
           "command": "/path/to/cdo-mcp/.venv/bin/fastmcp",
           "args": [
             "run",
             "/path/to/cdo-mcp/cdo_mcp.py"
           ]
         }
       }
     }
     ```

   * Replace `/path/to/cdo-mcp` with the actual path to your repository

1. Restart Claude Desktop

2. Interact with the CDO MCP via Claude Desktop

## Network Tools Guide

### Table of Contents

- [Inventory Management Tools](#inventory-management-tools)
- [cdFMC Management Tools](#cdfmc-management-tools)
- [Object Management Tools](#object-management-tools)
- [User Management Tools](#user-management-tools)

### Inventory Management Tools

- **GET /inventory/devices** - Retrieve a list of devices in the inventory
- **GET /inventory/managers** - Retrieve a list of managers (e.g., cdFMC)

### cdFMC Management Tools

- **GET /cdfmc/api/fmc_config/v1/domain/{domain_uuid}/policy/accesspolicies** - Retrieve a list of access policies
- **GET /cdfmc/api/fmc_config/v1/domain/{domain_uuid}/policy/accesspolicies/{policy_id}** - Fetch details of a specific access policy
- **GET /cdfmc/api/fmc_config/v1/domain/{domain_uuid}/policy/accesspolicies/{policy_id}/accessrules** - Fetch access rules for a policy
- **POST /cdfmc/api/fmc_config/v1/domain/{domain_uuid}/policy/accesspolicies/{policy_id}/accessrules** - Create a new access rule

### Object Management Tools

- **GET /objects** - Retrieve a list of objects (placeholder, update with actual endpoint)
- **POST /objects** - Create a new object (placeholder, update with actual endpoint)

### User Management Tools

- **GET /users** - Retrieve a list of users (placeholder, update with actual endpoint)

## Best Practices

- **Error Handling**: Check API responses for errors and handle them gracefully
- **Rate Limiting**: Implement delays to respect CDO API rate limits
- **Security**: Keep API tokens secure and rotate them regularly
- **Validation**: Use provided Pydantic schemas for data validation

## Troubleshooting

- **Authentication Errors**: Verify the API token and its permissions
- **Rate Limiting**: Implement delays if rate limit errors occur
- **Resource Not Found**: Ensure correct IDs (device, policy, rule) are used
- **Region Issues**: Confirm the correct regional base URL (e.g., `us`, `eu`, `apj`)

## Disclaimer

This software is provided "AS IS" without warranty. Use in production environments at your own risk. Ensure API tokens are stored securely and rotated regularly.

## About

Local MCP server for managing Cisco Defense Orchestrator resources via the CDO API. For full API details, refer to the [Cisco Defense Orchestrator API Documentation](https://docs.defenseorchestrator.com/).
