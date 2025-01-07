import pytest
from unittest.mock import Mock, AsyncMock
from repositories.git_hub_repo import GitHubRepo
from repositories.ai_analysis_repo import GPTRepository
from repositories.redis_repo import RedisRepository
from services.code_review import ReviewService
import httpx
from fastapi.exception_handlers import HTTPException

from unittest.mock import AsyncMock
import pytest
from unittest.mock import Mock, AsyncMock
from repositories.git_hub_repo import GitHubRepo
from repositories.ai_analysis_repo import GPTRepository
from repositories.redis_repo import RedisRepository
from services.code_review import ReviewService
import httpx
from fastapi.exception_handlers import HTTPException

from unittest.mock import AsyncMock, Mock



@pytest.mark.asyncio
async def test_process_repository_success(mocker):
    mock_github_repo = Mock()
    mock_github_repo.get_repo_files = AsyncMock(
        return_value=["https://example.com/file1.py", "https://example.com/file2.py"])
    mock_github_repo.get_file_content = AsyncMock(return_value="file content")
    mock_github_repo.is_valid_extension.return_value = True
    mock_github_repo.extract_repo_and_branch = Mock(return_value=("user/repo", "main"))

    mock_gpt_repo = Mock()
    mock_gpt_repo.generate_review.return_value = "Good code"
    mock_gpt_repo.generate_main_conclusion.return_value = "Overall good quality."

    mock_redis_repo = Mock()
    mock_redis_repo.get_cached_analysis_result.return_value = (None, None)
    mock_redis_repo.save_analysis_result.return_value = None

    # Instantiate the ReviewService
    review_service = ReviewService()
    review_service.github_repo = mock_github_repo
    review_service.gpt_repo = mock_gpt_repo
    review_service.redis_repo = mock_redis_repo

    repo_url = "https://github.com/user/repo"
    developer_level = "Junior"
    assignment_description = "Analyze code quality"

    # Call the method under test
    result = await review_service.process_repository(repo_url, developer_level, assignment_description)

    # Assertions to check the correctness of the result
    assert len(result.found_files) == 2
    assert result.found_files == ["file1.py", "file2.py"]
    assert len(result.downsides_comments) == 2
    assert result.downsides_comments[0]["comment"] == "Good code"
    assert result.rating == 2
    assert result.conclusion == "Overall good quality."
