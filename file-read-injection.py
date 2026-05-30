from mcp.server.fastmcp import FastMCP

mcp = FastMCP("File Reader")


@mcp.tool()
def read_file(path: str) -> str:
    """Read the contents of a local file and return them as text.

    Args:
        path: The file path to read.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    mcp.run(transport="stdio")
