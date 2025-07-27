// 通用函数
document.addEventListener('DOMContentLoaded', function() {
    // 自动关闭警告消息
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
    
    // 表格排序功能
    const sortableTables = document.querySelectorAll('.table-sortable');
    sortableTables.forEach(table => {
        const headers = table.querySelectorAll('th[data-sort]');
        headers.forEach(header => {
            header.style.cursor = 'pointer';
            header.addEventListener('click', () => {
                const sortKey = header.dataset.sort;
                const sortDirection = header.dataset.direction === 'asc' ? 'desc' : 'asc';
                
                // 重置所有表头的排序状态
                headers.forEach(h => {
                    h.dataset.direction = '';
                    h.querySelector('i')?.remove();
                });
                
                // 设置当前表头的排序状态
                header.dataset.direction = sortDirection;
                const icon = document.createElement('i');
                icon.className = `bi bi-sort-${sortDirection === 'asc' ? 'up' : 'down'} ms-1`;
                header.appendChild(icon);
                
                // 排序表格
                const tbody = table.querySelector('tbody');
                const rows = Array.from(tbody.querySelectorAll('tr'));
                
                rows.sort((a, b) => {
                    const aValue = a.querySelector(`td:nth-child(${Array.from(a.parentNode.children).indexOf(a) + 1})`).textContent;
                    const bValue = b.querySelector(`td:nth-child(${Array.from(b.parentNode.children).indexOf(b) + 1})`).textContent;
                    
                    if (sortDirection === 'asc') {
                        return aValue.localeCompare(bValue);
                    } else {
                        return bValue.localeCompare(aValue);
                    }
                });
                
                // 重新插入排序后的行
                rows.forEach(row => tbody.appendChild(row));
            });
        });
    });
});

// 表单验证增强
(function() {
    'use strict';
    
    // 获取所有需要验证的表单
    const forms = document.querySelectorAll('.needs-validation');
    
    // 阻止提交并应用验证
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            form.classList.add('was-validated');
        }, false);
    });
})();

// 快速预订功能
function quickReserve(roomId) {
    if (!roomId) return;
    
    // 打开快速预订模态框
    const modal = new bootstrap.Modal(document.getElementById('quickReserveModal'));
    
    // 设置会议室ID
    document.getElementById('quick_room_id').value = roomId;
    
    // 获取会议室名称
    const roomSelect = document.getElementById('room_id');
    const roomName = Array.from(roomSelect.options).find(option => option.value == roomId)?.textContent || '选中的会议室';
    
    // 更新模态框标题
    document.getElementById('quickReserveModalLabel').textContent = `快速预订 - ${roomName}`;
    
    modal.show();
}

// 日期格式化工具
function formatDate(date) {
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// 时间格式化工具
function formatTime(date) {
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
}
