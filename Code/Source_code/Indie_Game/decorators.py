from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .model.game import Game
from .model.update import Update  # 引入 Update 模型

def is_owner(view_func):
    def wrapper(request, *args, **kwargs):
        # 檢查 URL 中是否有 `update_id` 或 `game_id`
        if 'update_id' in kwargs:
            # 如果是操作 Update 模型，則通過 `update_id` 獲取 Update 實例
            update_instance = get_object_or_404(Update, pk=kwargs['update_id'])
            # 獲取 Update 關聯的 Homepage，再從 Homepage 獲取 Game
            homepage = update_instance.homepage
            game = homepage.game  # 獲取關聯的 Game
        elif 'id' in kwargs:
            # 如果是操作 Game 模型，則通過 `id` 獲取 Game 實例
            game = get_object_or_404(Game, pk=kwargs['id'])
        else:
            # 如果沒有 `id` 或 `update_id`，返回 403 禁止訪問
            return HttpResponseForbidden("Invalid request parameters.")
        
        # 確認 Game 的擁有者是否與當前用戶的 UserProfile 匹配
        if game.owner != request.user.userprofile:
            return HttpResponseForbidden("You are not allowed to access this resource.")
        
        # 如果檢查通過，則執行視圖函數
        return view_func(request, *args, **kwargs)

    return wrapper
