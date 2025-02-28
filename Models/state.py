# models/state.py
from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field

class AgentState(BaseModel):
    """
    Represents the state of the research process.
    """
    # Input
    query: str = Field(description="The original research query")
    
    # Research Navigator state
    sub_queries: List[str] = Field(default_factory=list, description="Decomposed sub-queries")
    search_results: List[Dict[str, Any]] = Field(default_factory=list, description="Raw search results")
    research_complete: bool = Field(default=False, description="Whether research phase is complete")
    
    # Data Synthesis state
    synthesized_data: Dict[str, Any] = Field(default_factory=dict, description="Processed and integrated information")
    synthesis_complete: bool = Field(default=False, description="Whether synthesis phase is complete")
    
    # Content Delivery state
    final_content: Optional[str] = Field(default=None, description="Final formatted research output")
    content_complete: bool = Field(default=False, description="Whether content delivery phase is complete")
    
    # Metadata
    iteration_count: int = Field(default=0, description="Number of iterations through the workflow")
    error_log: List[str] = Field(default_factory=list, description="Logs of any errors encountered")